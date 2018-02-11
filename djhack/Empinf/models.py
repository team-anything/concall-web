from django.db import models
# from Department.models import Dept
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=264)
    emid = models.IntegerField(default=1,unique = True)
    slug = models.SlugField(default='none')
    total_issues = models.IntegerField(default=0)
    issues_pending = models.IntegerField(default=0)
    avg_rating = models.IntegerField(default=0)
    #dept = models.ForeignKey(Dept)


    def __str__(self):
        return self.name

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic)
#     name = models.CharField(max_length = 264,unique = True)
#     url = models.URLField(unique = True)

    # def __str__(self):
    #     return self.name
