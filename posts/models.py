from django.db import models
from django.conf import settings


# Create your models here.
class Posts(models.Model):

    title = models.CharField(max_length=150, db_index=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    data = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    unlike = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['data']