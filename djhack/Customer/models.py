from django.db import models
# Create your models here.
class Cust(models.Model):
    name = models.CharField(max_length=264)
    cuid = models.IntegerField(default=1,unique = True)
    total_issues = models.IntegerField(default=0)



    def __str__(self):
        return self.name

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic)
#     name = models.CharField(max_length = 264,unique = True)
#     url = models.URLField(unique = True)

    # def __str__(self):
    #     return self.name
