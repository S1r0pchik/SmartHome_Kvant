from django.db import models


class on_off_position(models.Model):
    position = models.TextField()

    def __str__(self):
        return self.position