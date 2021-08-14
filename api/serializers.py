from rest_framework import serializers

from .models import CustomUser, Bucket, BucketItem


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user
    """
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['id','email']


class BucketItemSerializer(serializers.ModelSerializer):
    """
    serializer for bucket item
    """
    class Meta:
        model = BucketItem
        fields = '__all__'
        read_only_fields = ["bucket",]


class BucketSerializer(serializers.ModelSerializer):
    """
    serializer for bucket
    """
    items = BucketItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Bucket
        fields = '__all__'
        read_only_fields = ['user',]
