from django.db import models

# Create your models here.
class deparment(models.Model):
    name = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.name
    

class employee(models.Model):
    name = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    deparment_name = models.ForeignKey(deparment,blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
