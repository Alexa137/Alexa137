from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

class Account(models.Model):
    email = models.EmailField(unique=True, blank=False)
    account_id = models.CharField(unique=True, max_length=50, blank=False)
    account_name = models.CharField(max_length=100, blank=False)
    app_secret_token = models.CharField(unique=True, max_length=100, blank=True, editable=False, default=uuid.uuid4().hex)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.account_name
    
class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=False)
    http_method = models.CharField(max_length=10, choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT')], blank=False)
    headers = models.JSONField(default=dict)

    def __str__(self):
        return self.url



# class AccountManager(BaseUserManager):
#     def create_user(self, email, account_name, password=None, website=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         account = self.model(
#             email=self.normalize_email(email),
#             account_name=account_name,
#             website=website
#         )

#         account.set_password(password)
#         account.save(using=self._db)
#         return account

#     def create_superuser(self, email, account_name, password, website=None):
#         account = self.create_user(
#             email=self.normalize_email(email),
#             account_name=account_name,
#             password=password,
#             website=website
#         )
#         account.is_admin = True
#         account.save(using=self._db)
#         return account


# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     account_name = models.CharField(max_length=255)
#     app_secret_token = models.CharField(max_length=255, default=secrets.token_hex)
#     website = models.URLField(blank=True)

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = AccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['account_name']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin