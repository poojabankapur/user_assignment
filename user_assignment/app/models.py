from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The username must be set'))

        new_user = self.model(username=username, first_name=first_name, last_name=last_name, **extra_fields)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, username, first_name, last_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, first_name, last_name, password, **extra_fields)


class User(AbstractUser):
    """
        User Class.
        Represents the social account.
    """
    id = models.AutoField(primary_key=True, help_text="The user's unique ID.")
    username = models.CharField(verbose_name='username', max_length=64, null=False, unique=True,
                                help_text="The user's chosen username. Used to login, for example.")
    first_name = models.CharField(verbose_name='first name', max_length=20, null=False,
                                  help_text="The user's first name.")
    last_name = models.CharField(verbose_name='last name', max_length=40, null=False,
                                 help_text="The user's last name.")
    password = models.CharField(verbose_name=_('password'), max_length=255, blank=True,
                                help_text=_("The user's password."))
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name