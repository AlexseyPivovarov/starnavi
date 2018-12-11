from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import Response

from .models import Posts
from .serializer import PostSerializer, LikeSerializer


# Create your views here.
class CreatePost(CreateAPIView):

    model = Posts
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddLikeView(UpdateAPIView):

    queryset = Posts.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'title'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={'like': instance.like + 1}, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class AddUnlikeView(UpdateAPIView):

    queryset = Posts.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'title'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={'unlike': instance.unlike + 1}, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)




