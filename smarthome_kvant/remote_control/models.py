from django.db import models


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


class LedName(models.Model):
    add_name = models.TextField()

    def __str__(self):
       return self.add_name


class PosTerm(models.Model):
    pos_term = models.TextField()

    def __str__(self):
       return self.pos_term