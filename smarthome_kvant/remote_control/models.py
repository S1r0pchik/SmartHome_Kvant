from django.db import models


class on_off_position(models.Model):
    position = models.TextField()

    def __str__(self):
       return self.position
class trm(models.Model):
    izm1 = models.IntegerFieldField()
    izm2 = models.IntegerFieldField()
    izm3 = models.IntegerFieldField()
    izm4 = models.IntegerFieldField()
    izm5 = models.IntegerFieldField()