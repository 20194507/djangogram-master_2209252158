from rest_framework import serializers

from djangogram.users.models import User as user_model
from . import models


class FeedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = (
            "id",
            "username",
            "profile_photo",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Comment
        fields = (
            "id",
            "contents",
            "author",
        )


class PostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True)
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Post
        fields = (
            "id",
            # djangogam "image",
            "cooking_time", # 수정_2207052004
            "image_01",
            "image_02", # 일시 수정_2206272310
            "country", # 수정_2207262128
            "caption",
            "comment_post",
            "author",
            "image_likes",
        )
