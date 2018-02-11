from django.db import models
from Empinf.models import Employee
from Customer.models import Cust
# Create your models here.

class Iss(models.Model):
    title = models.CharField(max_length=264)
    issueid = models.IntegerField(default=1,unique = True)
    agent = models.ForeignKey(Employee)
    cust=models.ForeignKey(Cust)
    priority = models.IntegerField(default=2)
    complaint_date = models.DateTimeField(auto_now_add=True)
    #issues_pending = models.IntegerField(default=0)
    #avg_rating = models.IntegerField(default=0)
    summary = models.CharField(max_length=1024,default='unassigned')
    resolve = models.BooleanField(default='False')

    def __str__(self):
        return self.title

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic)
#     name = models.CharField(max_length = 264,unique = True)
#     url = models.URLField(unique = True)

    # def __str__(self):
    #     return self.name
