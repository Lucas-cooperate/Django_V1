from django.db import models


# Create your models here.
class Demo(models.Model):
    count = models.IntegerField(verbose_name="数量")
