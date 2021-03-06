from django.conf import settings

from appconf import AppConf


class AccountAppConf(AppConf):
    
    OPEN_SIGNUP = True
    LOGIN_URL = "account_login"
    SIGNUP_REDIRECT_URL = "/"
    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"
    PASSWORD_CHANGE_REDIRECT_URL = "/"
    PASSWORD_RESET_REDIRECT_URL = "account_login"
    USER_DISPLAY = lambda user: user.username
    EMAIL_UNIQUE = True
    EMAIL_CONFIRMATION_REQUIRED = False
    EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
    EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_login"
    EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
    SETTINGS_REDIRECT_URL = "account_settings"
    CONTACT_EMAIL = "support@example.com"
