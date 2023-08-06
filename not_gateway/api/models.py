from django.db import models


class EmailConfig(models.Model):
    """
    Email congiguration model to store different configurations.
    """

    class Meta:
        unique_together = ['name', 'host', 'port', 'password', 'sent_as']

    name = models.CharField(null=False, max_length=128)
    host = models.CharField(null=False, max_length=128)
    port = models.CharField(null=False, max_length=128)
    password = models.CharField(null=False, max_length=128)
    sent_as = models.EmailField(null=False)
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)


class Email(models.Model):
    """
    Email model to register emails.
    """

    class Meta:
        unique_together = ['name', 'key', 'subject', 'body']

    name = models.CharField(null=False, unique=True, max_length=128)
    key = models.CharField(null=False, unique=True, max_length=128)
    subject = models.CharField(null=False, max_length=128)
    body = models.CharField(null=False, max_length=128)
    attachements = models.CharField(null=False, max_length=128)
    active = models.BooleanField(default=True)
    config = models.ForeignKey(EmailConfig, null=False, on_delete=models.CASCADE)


class EmailSubscriber(models.Model):
    """
    Email Subscriber model to store all the subscribers for different emails
    """

    class Meta:
        unique_together = ['name', 'user_email', 'email']

    name = models.CharField(null=False, max_length=128)
    user_email = models.EmailField(null=False)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
