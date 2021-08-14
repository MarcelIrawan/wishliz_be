from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    override django user model with custom setting
    change username field to email field
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email


class Bucket(models.Model):
    """
    bucket model
    """
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)

    bucket_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{ self.user} : { self.bucket_name }"


class BucketItem(models.Model):
    """
    bucket item model
    """
    item_name = models.CharField(max_length=50)

    price = models.PositiveBigIntegerField(blank=True,
                                           null=True)

    desc = models.TextField(blank=True,
                            null=True)

    pict = models.ImageField(upload_to='item_images/',
                             blank=True,
                             null=True)

    shop_link = models.URLField(blank=True,
                                null=True)

    bucket = models.ForeignKey(Bucket,
                               on_delete=models.CASCADE,
                               related_name='items')

    def __str__(self):
        return f"{ self.bucket } : { self.item_name }"
