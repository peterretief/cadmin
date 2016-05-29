from django.db import models

from django.utils import timezone


class Client(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fullname

# Create your models here.
