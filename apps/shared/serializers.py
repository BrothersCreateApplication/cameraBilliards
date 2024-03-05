from rest_framework import serializers
from datetime import datetime
import pytest


class ErrorResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    error_code = serializers.CharField()


class TimestampField(serializers.DateTimeField):
    def to_internal_value(self, value):
        converted = datetime.fromtimestamp(value/1000).replace(microsecond=value%1000*1000)
        return super(TimestampField, self).to_representation(converted)