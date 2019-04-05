from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    # changes email to unique and blank to false
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['username']
