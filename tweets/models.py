from django.db import models

class Tweet(models.Model):
    #id = models.AutoField(primary_key=True) by default.
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
