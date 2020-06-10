from django.db import models

# Create your models here.

class EmailSchedule(models.Model):
    to_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    exec_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

