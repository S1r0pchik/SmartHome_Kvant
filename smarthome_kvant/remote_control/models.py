from django.db import models


class on_off_position(models.Model):
    position = models.TextField()

    def __str__(self):
       return self.position


class Termometr(models.Model):
    time = models.TextField()
    temp = models.TextField()

    def __str__(self):
       return self.time + " " + self.temp

class trm(models.Model):
    izm1 = models.IntegerField()
    izm2 = models.IntegerField()
    izm3 = models.IntegerField()
    izm4 = models.IntegerField()
    izm5 = models.IntegerField()

class rgb(models.Model):
    r = models.IntegerField()
    g = models.IntegerField()
    b = models.IntegerField()
