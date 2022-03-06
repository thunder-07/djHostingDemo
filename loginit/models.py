from django.db import models

# Create your models here.
class saver(models.Model):
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
