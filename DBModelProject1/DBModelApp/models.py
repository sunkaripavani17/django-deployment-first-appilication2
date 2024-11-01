from django.db import models


# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField();
    ename = models.CharField(max_length=30);
    esal = models.FloatField();
    eaddr = models.CharField(max_length=30);
    def __str__(self):
        ss=str(self.eno)+"\t"+str(self.ename)+"\t"+str(self.esal)+"\t"+str(self.eaddr);
        return (ss);

class Company(models.Model):
    compid=models.IntegerField();
    compname=models.CharField(max_length=50);
    noofemps=models.IntegerField();
    compaddr=models.CharField(max_length=50);
    def __str__(self):
        ss=str(self.compid)+"\t"+str(self.compname)+"\t"+str(self.noofemps)+"\t"+str(self.compaddr);
        return (ss);

