from fabric.connection import Connection
from fabric import task
import os
from dotenv import load_dotenv
load_dotenv('.env')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log(text, bcolor):
    print(bcolor + text + bcolors.ENDC)


def run_test(ctx):
    log("Start running unit tests", bcolors.HEADER)
    with ctx.prefix("source ./venv/bin/activate"):
        ctx.run("pytest")
        log("All unit tests passed", bcolors.OKGREEN)


def connect_to_ec2():
    try:
        log("Connecting to server", bcolors.HEADER)
        conn = Connection(host=f'root@{os.getenv("HOSTING_DOMAIN")}' , connect_kwargs={"password": os.getenv("HOSTING_PASSWORD") })
        log("Connect to server successfully", bcolors.OKGREEN)
        return conn
    except Exception as e:
        log("Connect to server failed\nError:\n", bcolors.FAIL)
        print(e)
        return None


def pull_and_run_project(conn):
    log("Enable virtual environment and cd to project folder", bcolors.HEADER)
    venv_prefix = "source /usr/local/lsws/Example/html/bin/activate"
    with conn.cd("/usr/local/lsws/Example/html/camera-billiards"):
        with conn.prefix(venv_prefix):
            log("Pull latest code from main branch", bcolors.HEADER)
            conn.run("git checkout main")
            conn.run("git pull")
            log("Install requirements.txt", bcolors.HEADER)
            conn.run("pip3 install -r requirements.txt")
            log("Start to migrate", bcolors.HEADER)
            conn.run("python manage.py migrate")
            log("Reload lsws", bcolors.HEADER)
            conn.run("sudo killall lswsgi")


@task
def deploy(ctx):
    run_test(ctx)
    conn = connect_to_ec2()
    if conn:
        pull_and_run_project(conn)
        log("Deploy successfully", bcolors.OKGREEN)
