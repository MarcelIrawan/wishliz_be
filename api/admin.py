from django.contrib import admin

from .models import Bucket, BucketItem

admin.site.register(Bucket)
admin.site.register(BucketItem)