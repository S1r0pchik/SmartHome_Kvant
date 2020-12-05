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


class Led(models.Model):
    pos = models.TextField()
    number = models.TextField()
    name = models.TextField()

    def __str__(self):
       return self.pos + " " + self.number + " " + self.name