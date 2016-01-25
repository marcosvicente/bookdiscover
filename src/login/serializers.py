from rest_framework import serializers
from .models import Account

class AccountSerializers(serializers.Serializer):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Account.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.title)
        instance.username = validated_data.get('username', instance.code)
        instance.first_name = validated_data.get('first_name', instance.linenos)
        instance.last_name = validated_data.get('last_name', instance.language)
        instance.save()
        return instance
