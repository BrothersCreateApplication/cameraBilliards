import pytest
from apps.shared.serializers import TimestampField


@pytest.mark.django_db
class TestTimestampField:
    def test_to_internal_value(self):
        # given
        sut = TimestampField()
        # when
        result = sut.to_internal_value(1375340400123)
        # then
        assert result == '2013-08-01T07:00:00.123000Z'
