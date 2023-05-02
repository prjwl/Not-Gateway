from django.db import models

class EmailConfig(models.Model):

    name = models.CharField(null=False)
    host = models.CharField(null=False)
    port = models.CharField(null=False)
    password = models.CharField(null=False)
    sent_as = models.EmailField(null=False)
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)
