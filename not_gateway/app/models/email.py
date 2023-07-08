from django.db import models
from .email_config import EmailConfig


class EmailManager(models.Manager):
    pass

class Email(models.Model):
    """
    Email model to register emails.
    """

    class Meta:
        unique_together =  ['name', 'key', 'subject', 'body']


    name = models.CharField(null=False, unique=True)
    key = models.CharField(null=False, unique=True)
    subject = models.CharField(null=False)
    body = models.CharField(null=False)
    attachements = models.CharField(null=False)
    active = models.BooleanField(default=True)
    config = models.ForeignKey(EmailConfig, null=False, on_delete=models.CASCADE)