from django.utils.translation import ugettext_lazy as _

ASSERT_USER_EMAIL_FIELD_EXISTS = _(
    'User model has to implement a `get_email_field_name` method. '
    'https://docs.djangoproject.com/en/2.0/topics/auth/customizing/'
    '#django.contrib.auth.models.AbstractBaseUser.get_email_field_name'
)

INVALID_CREDENTIALS_ERROR = _('Unable to login with provided credentials.')
INACTIVE_ACCOUNT_ERROR = _('User account is disabled.')
INVALID_TOKEN_ERROR = _('Invalid token for given user.')
INVALID_UID_ERROR = _('Invalid user id or user doesn\'t exist.')
STALE_TOKEN_ERROR = _('Stale token for given user.')
PASSWORD_MISMATCH_ERROR = _('The two password fields didn\'t match.')
USERNAME_MISMATCH_ERROR = _('The two {0} fields didn\'t match.')
INVALID_PASSWORD_ERROR = _('Invalid password.')
EMAIL_NOT_FOUND = _('User with given email does not exist.')
CANNOT_CREATE_USER_ERROR = _('Unable to create account.')
USER_WITHOUT_EMAIL_FIELD_ERROR = _(
    'User model does not contain specified email field. '
    'Please see http://djoser.readthedocs.io/en/latest/settings.html#'
    'USER_EMAIL_FIELD_NAME for more details.'
)
TOKEN_MODEL_NONE_ERROR = _(
    'Token model has not been configured in settings. Visit '
    'https://djoser.readthedocs.io/en/latest/settings.html#token-model '
    'for reference.'
)
