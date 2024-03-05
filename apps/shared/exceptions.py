from rest_framework import status
from rest_framework.exceptions import APIException
from .serializers import ErrorResponseSerializer
import pytest


class CameraBilliardsAPIException(APIException):
    default_message = "Unknown error."
    default_code = "unknown_error"

    def __init__(self, error, status_code=status.HTTP_400_BAD_REQUEST):
        self.status_code = status_code
        self.detail = error.serialize()


class BaseError(object):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def swagger_description(self):
        return "<font size='2'><b>error_code</b> <i>{0}</i>\n <b>message</b> <i>{1}</i></font>".format(
            self.error_code, self.message
        )

    def serialize(self):
        return {"message": self.message, "error_code": self.error_code}
