from django.db import models

# Create your models here.

class StudentData(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name
    class Meta:
        db_table="forms_data"
        
