from rest_framework import serializers

from facebook_v22.models import Comment


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    username = serializers.CharField()
    registration_date = serializers.DateTimeField()


class PostSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    message = serializers.CharField()
    post_date = serializers.DateTimeField()
    user = UserSerializer()


class CommentDeepSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'message', 'comment_date']


class CommentShallowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'message', 'comment_date']
