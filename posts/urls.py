from django.urls import path

from .views import CreatePost, AddLikeView, AddUnlikeView


urlpatterns = [
    path('add/', CreatePost.as_view()),
    path('like/<str:title>/', AddLikeView.as_view()),
    path('unlike/<str:title>/', AddUnlikeView.as_view()),
]