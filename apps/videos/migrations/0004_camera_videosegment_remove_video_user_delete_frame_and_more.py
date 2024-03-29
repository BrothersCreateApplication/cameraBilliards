# Generated by Django 4.2.7 on 2024-03-19 02:38

import apps.flax_id.django.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0003_video_video_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Camera",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=255,
                    ),
                ),
                ("model_type", models.CharField(blank=True, max_length=255, null=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("ip_address", models.CharField(blank=True, max_length=255, null=True)),
                ("username", models.CharField(blank=True, max_length=255, null=True)),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="VideoSegment",
            fields=[
                (
                    "id",
                    apps.flax_id.django.fields.FlaxId(
                        editable=False, max_length=16, primary_key=True, serialize=False
                    ),
                ),
                ("description", models.CharField(max_length=255)),
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                (
                    "video_file",
                    models.FileField(blank=True, null=True, upload_to="videos/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "camera",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="videos.camera"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="video",
            name="user",
        ),
        migrations.DeleteModel(
            name="Frame",
        ),
        migrations.DeleteModel(
            name="Video",
        ),
    ]
