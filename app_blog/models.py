from django.db import models
from app_admin.models import UserProfile
import uuid

# Create your models here.
class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    category = models.CharField(max_length=50, null=False, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        UserProfile,
        default="4587b55c-fe60-468a-8c19-302fe584e7ce",
        on_delete=models.CASCADE,
    )
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.title
