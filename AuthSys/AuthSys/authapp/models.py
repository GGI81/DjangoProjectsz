from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import models as auth_models

from AuthSys.authapp.manager import AppUserManager
from AuthSys.authapp.validators import validate_only_letters_numbers_underscores, validate_only_letters

"""
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model -> settings.py 'auth_app.AppUser'
3. Create user manager
"""


class AuthUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=(
            validate_only_letters_numbers_underscores,
        ),
    )

    email = models.EmailField()

    # date_joined = models.DateTimeField(
    #     auto_now_add=True,
    # )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = AppUserManager()


class UserProfile(models.Model):
    NAME_MAX_LEN = 25
    NAME_MIN_LEN = 2
    
    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validate_only_letters,
            MinLengthValidator(NAME_MIN_LEN),
        ),
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validate_only_letters,
            MinLengthValidator(NAME_MIN_LEN),
        ),
    )

    email = models.EmailField()

    user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
