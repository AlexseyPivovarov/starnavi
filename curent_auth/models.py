from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator

from .managers import UserManager


# Create your models here.
class CustomUser(AbstractUser):

    email_validator = EmailValidator()

    username = models.EmailField(
        _('email'),
        max_length=150,
        unique=True,
        help_text=_('Required. Valid email. Letters, digits and @/./+/-/_ only.'),
        validators=[email_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = None

    objects = UserManager()

    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.username], **kwargs)