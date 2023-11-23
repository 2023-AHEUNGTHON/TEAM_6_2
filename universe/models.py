from django.db import models

# Create your models here.
class Write(models.Model):
    content=models.TextField()
    category=models.CharField(max_length=20,null=True)
    def __str__(self):
        return f'{self.content} [{self.id}]'
    