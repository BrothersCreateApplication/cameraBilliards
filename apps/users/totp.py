import time

from django.utils import timezone

from pyotp import TOTP as BaseTOTP
from pyotp import utils


class TOTP(BaseTOTP):
    """
    This is a fork from pyotp to use our project's \
    timezone settings as part of the OTP generation process.
    """

    def now(self):
        """
        Return an OTP generated now.
        """
        return self.generate_otp(self.timecode(timezone.now()))

    def verify(self, otp, for_time=None, check_before=0, check_after=0):
        """
        Verify validates the OTP.

        Args:
            check_before (int): The validity window of how many \
                                ticks before to check for.\
                                This is to allow for minor clock \
                                synchronisation issues.

            check_after (int): The validity window of how many \
                                ticks after to check for.\
                                This is to allow for minor clock \
                                synchronisation issues.

            for_time (datetime): Ths time to check against. \
                                 This defaults to the current \
                                 timezone aware datetime.
        Returns:
            bool: The return value. True for success, False otherwise.

        """
        if for_time is None:
            for_time = timezone.now()

        if check_before or check_after:
            for i in range(-check_before, check_after + 1):
                if utils.strings_equal(str(otp), str(self.at(for_time, i))):
                    return True
            return False

        return utils.strings_equal(str(otp), str(self.at(for_time)))
