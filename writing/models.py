from django.db import models
from users.models import User


class Writing(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writing")
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    pending_approval = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    date_approved = models.DateTimeField(null=True, blank=True)
    failed_approval = models.BooleanField(default=False)
    date_failed = models.DateTimeField(null=True, blank=True)
    reason_failed = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_approved']

    def __str__(self):
        return self.title