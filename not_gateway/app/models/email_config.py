from django.db import models


class EmailConfigManager(models.Manager):
    pass


class EmailConfig(models.Model):
    """
    Email congiguration model to store different configurations.
    """

    class Meta:
        unique_together = ['name', 'host', 'port', 'password', 'sent_as']

    name = models.CharField(null=False)
    host = models.CharField(null=False)
    port = models.CharField(null=False)
    password = models.CharField(null=False)
    sent_as = models.EmailField(null=False)
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)

    objects = EmailConfigManager()
