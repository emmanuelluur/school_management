from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    card_id = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name
