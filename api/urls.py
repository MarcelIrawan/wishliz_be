from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BucketUserBased, BucketItemCreate, BucketItemUpdateDelete


router = DefaultRouter()

router.register(r'bucket',
                BucketUserBased,
                basename="bucket for user")

router.register(r'item',
                BucketItemUpdateDelete,
                basename='Item Update and Delete')

urlpatterns = [
    path('', include(router.urls)),

    path('bucket/<int:bucket_pk>/item',
         BucketItemCreate.as_view(),
         name='Item on bucket')
]
