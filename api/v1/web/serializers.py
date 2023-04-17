from dataclasses import fields
from rest_framework import serializers
from web.models import About, Gallery, Services


class ViewAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = (
            'id',
            'name',
            'description',
            'photo',
            'is_deleted'
            )


class ViewServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = (
            'id',
            'name',
            'description',
            'photo',
            'is_deleted'
            )


class GalleryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = (
            'id',
            'photo',
        )


class AddEnquiriesSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()


class AddAboutSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.FileField()


class AddServiceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.FileField()


class AddGallerySerializer(serializers.Serializer):
    photo = serializers.FileField()