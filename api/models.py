from django.db import models

# Create your models here.
class Echo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['created']