from django.db import models

# Create your models here.
class UserInsightRecord(models.Model):
    user_email = models.CharField(
        null=False,
        blank=False,
        max_length=200
    )
    description = models.CharField(
        null=False,
        blank=False,
        max_length=2000,
        help_text="A description of the Insight that was sent to the user via email."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )