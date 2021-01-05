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

class Rgb(models.Model):
    r = models.IntegerField(null = True)
    g = models.IntegerField(null = True)
    b = models.IntegerField(null = True)

    def __srt__(self):
        return self.r + ' ' + self.g + ' ' + self.b


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    name = models.TextField(
        verbose_name="Имя пользователяы",
        null=True,
        blank=True
    )
    def __str__(self):
        return f'#{self.external_id} {self.name}'
    class Meta:
        verbose_name = "Профиль Телеграмм"
        verbose_name_plural = "Профили Телеграмм"

class Message(models.Model):
    profile = models.ForeignKey(
        to='remote_control.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    created_at = models.DateTimeField(
        verbose_name="Время получания",
        auto_now_add=True
    )
    def __str__(self):
        return f"Сообщения {self.pk} от {self.profile}"
    class Meta:
        verbose_name = "Сообщения с тг бота"
        verbose_name_plural = "Сообщения с тг бота"