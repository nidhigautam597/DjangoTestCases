from django.db import models

# Create your models here.
class insertemprecord(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    class Meta:
        db_table="emp"
