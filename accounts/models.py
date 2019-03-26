from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('username must have an email address')
        user = self.model(username=username, email=email,
                          first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name,  username, email, password=None):
        user = self.create_user(first_name, last_name,
                                username, email, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    # image = models.ImageField()
    username = models.CharField(max_length=300,
                                validators=[
                                    RegexValidator(
                                        regex=USERNAME_REGEX,
                                        message="Username Must be alphanumeric or contain numbers",
                                        code='invalid_username'
                                    )],
                                unique=True)
    email = models.EmailField(unique=True, verbose_name="email address")
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def has_module_perms(self, perm, obj=None):
        return True

    def has_perm(self, app_label):
        return True

    def __str__(self):
        return self.email

    def get_short_name(self):
        return f"{self.first_name} {self.last_name}"
