from django.db import models


class on_off_position(models.Model):
    position = models.IntegerField()

    def __str__(self):
        return self.position