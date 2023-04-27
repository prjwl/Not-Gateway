from django.db import models
from .email import Email

class EmailSubscriber(models.Model):
    name = models.CharField(null=False)
    email_id = models.EmailField(null=False)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)