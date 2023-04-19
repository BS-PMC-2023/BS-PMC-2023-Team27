from django.db import models

# Create your models here.
class USER(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class Meta:
        db_table="user"