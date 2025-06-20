from django.conf import settings
from django.db import models

USER = settings.AUTH_USER_MODEL


class Document(models.Model):
    owner = models.ForeignKey(USER, on_delete=models.CASCADE)
    title = models.CharField(default="Title")
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
