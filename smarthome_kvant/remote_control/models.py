from django.db import models


class on_off_position(models.Model):
    position = models.TextField()

    #def __str__(self):
       #return self.position

class temp_on_off(models.Model):
    position = models.IntegerField()

