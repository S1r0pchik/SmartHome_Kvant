from django.db import models


class on_off_position(models.Model):
    position = models.TextField()
    def __str__(self):
        template = '{0.position}'
        return template.format(self)

class temp_on_off(models.Model):
    position = models.IntegerField()
    temp = models.IntegerField(null=True)
    def __str__(self):
        template = '{0.position} {0.temp}'
        return template.format(self)