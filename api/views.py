from rest_framework import (mixins,
                            viewsets,
                            generics,
                            filters)
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Bucket, BucketItem, CustomUser
from .serializers import BucketSerializer, BucketItemSerializer


class BucketUserBased(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    bucket based on user
    """
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Bucket.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class BucketItemCreate(generics.CreateAPIView):
    """
    viewset for bucket item
    """
    queryset = BucketItem.objects.all()
    serializer_class = BucketItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        bucket_pk = self.kwargs.get("bucket_pk")
        bucket = get_object_or_404(Bucket, pk=bucket_pk)
        serializer.save(bucket=bucket)


class BucketItemUpdateDelete(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    """
    viewset for update and delete item
    """
    queryset = BucketItem.objects.all()
    serializer_class = BucketItemSerializer
    permission_classes = [IsAuthenticated]
