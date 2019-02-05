from django.db import models

class Pet(models.Model):
    SEX_CHOICES=[('M','Male'),('F','Female')]
    sex=models.CharField(choices=SEX_CHOICES,max_length=1,blank=True)
    name=models.CharField(max_length=200)
    age=models.IntegerField(null=True)
    species=models.CharField(max_length=200)
    breed=models.CharField(max_length=30,blank=True)
    description=models.TextField()
    vaccinations=models.ManyToManyField('Vaccine',blank=True)
    submission_date=models.DateTimeField()
    submitter=models.TextField(max_length=200)

class Vaccine(models.Model):
    name=models.CharField(max_length=50)