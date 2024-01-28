from django.db import models

# Create your models here.

class student(models.Model):
    choices = [
        ('Computing','Computing'),
        ('Medcine','Medcine'),
        ('Health science','Health science'),
        ('Engineering','Engineering'),
        ('Account','Account')
    ]
    student_id= models.CharField(max_length=100,unique=True,verbose_name="ID")
    name = models.CharField(max_length=400)
    Date=models.DateField()
    Faculty = models.CharField(max_length=100,choices=choices, null=False,blank=False)
    Phone = models.CharField(max_length=20,null=True,blank=True)
    ADDRESS = models.CharField(max_length=200)
    nex = models.CharField(max_length=150)

    def __str__(self):
        return self.name