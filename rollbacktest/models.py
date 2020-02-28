from django.db import models

# Create your models here.

class People(models.Model):
    name=models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.name

