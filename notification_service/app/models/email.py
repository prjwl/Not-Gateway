from django.db import models

class Email(models.Model):
    name = models.CharField(null=False)
    key = models.CharField(null=False)
    subject = models.CharField(null=False)
    body = models.CharField(null=False)
    attachements = models.CharField(null=False)
    active = models.BooleanField(default=True)