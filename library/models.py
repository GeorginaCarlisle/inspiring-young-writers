from django.db import models
from users.models import User
from writing.models import Writing


class Feedback(models.Model):
    giver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="given_feedback")
    writing = models.ForeignKey(
        Writing,
        on_delete=models.CASCADE,
        related_name="received_feedback")
    star_one = models.TextField()
    star_two = models.TextField()
    wish = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_edit = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    date_approved = models.DateTimeField(null=True, blank=True)
    failed_approval = models.BooleanField(default=False)
    date_failed = models.DateTimeField(null=True, blank=True)
    reason_failed = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date_approved']

    def __str__(self):
        return f'Feedback for {self.writing} by {self.giver}'
