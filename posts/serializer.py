from rest_framework.serializers import ModelSerializer, CharField

from .models import Posts


class PostSerializer(ModelSerializer):

    class Meta:
        model = Posts
        fields = ('title', 'body')


class LikeSerializer(ModelSerializer):

    class Meta:
        model = Posts
        fields = ('title', 'like', 'unlike')
