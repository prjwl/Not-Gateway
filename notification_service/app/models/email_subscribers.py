from django.db import models
from .email import Email

class EmailSubscriberManager(models.Manager):
    pass


class EmailSubscriber(models.Model):
    """
    Email Subscriber model to store all the subscribers for different emails
    """
    class Meta:
        unique_together = ['name', 'email_id', 'email']


    name = models.CharField(null=False)
    email_id = models.EmailField(null=False)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    objects = EmailSubscriberManager()