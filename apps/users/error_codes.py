from enum import Enum
from apps.shared.exceptions import BaseError


class UserErrorCode(Enum):
    LOGIN_INVALID = BaseError("Invalid full name or password.", "user_login_invalid")
    LOGIN_PARAM_INVALID = BaseError(
        "Body must have 'email' and 'password' fields.", "user_login_params_invalid"
    )
    REGISTER_EMAIL_EXIST = BaseError(
        "User with this email already exists.", "user_register_email_exist"
    )
    REGISTER_PASSWORD_INVALID = BaseError(
        "Password must be at least 6 characters.", "user_register_password_invalid"
    )
    REGISTER_FULL_NAME_REQUIRED = BaseError(
        "Full name is required.", "user_register_username_required"
    )
    REGISTER_GENDER_INVALID = BaseError(
        "Gender must be 'male', 'female' or 'other'.", "user_register_gender_invalid"
    )
    REQUEST_FORGOT_PASSWORD_EMAIL_INVALID = BaseError(
        "There is no existing user with this email.",
        "user_request_forgot_password_email_invalid",
    )
    VERIFY_OTP_EMAIL_INVALID = BaseError(
        "There is no existing user with this email.",
        "user_verify_otp_email_invalid",
    )
    VERIFY_OTP_INVALID = BaseError(
        "OTP code is invalid or expire.",
        "user_verify_otp_invalid",
    )
    VERIFY_OTP_FAILURE_COUNT_MORE_THAN_MAXIMUM = BaseError(
        "OTP failure verification is more than maximum.",
        "user_verify_otp_failure_count_more_than_maximum",
    )
    SET_NEW_PASSWORD_INVALID = BaseError(
        "Password must be at least 6 characters.",
        "user_set_new_password_invalid",
    )
    CHANGE_PASSWORD_INVALID = BaseError(
        "Password must be at least 6 characters.",
        "user_change_password_invalid",
    )
    CHANGE_PASSWORD_CURRENT_PASSWORD_INCORRECT = BaseError(
        "Current password is incorrect.",
        "user_change_password_current_password_incorrect",
    )
    LOGIN_FACEBOOK_INVALID_ACCESS_TOKEN = BaseError(
        "Access token is invalid.",
        "user_login_facebook_invalid_access_token",
    )
    LOGIN_APPLE_INVALID_ACCESS_TOKEN = BaseError(
        "Access token is invalid.",
        "user_login_apple_invalid_access_token",
    )
    LOGIN_APPLE_INCONSISTENT_EMAIL = BaseError(
        "Email is inconsistent.",
        "user_login_apple_inconsistent_email",
    )
    SUBMIT_IOS_RECEIPT_DATA_FAILED = BaseError(
        "Receipt data is not valid",
        "submit_ios_receipt_data_failed",
    )
    USER_HAS_BEEN_BLOCKED = BaseError(
        "Your account is blocked because you violate our terms of use",
        "user_has_been_blocked",
    )
    INVALID_ACCESS_TOKEN = BaseError(
        "Your account is already logged in somewhere else, please login again",
        "invalid_access_token",
    )