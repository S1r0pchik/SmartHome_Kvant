# Generated by Django 3.1.4 on 2020-12-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0004_rgb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rgb',
            name='b',
        ),
        migrations.RemoveField(
            model_name='rgb',
            name='g',
        ),
        migrations.RemoveField(
            model_name='rgb',
            name='r',
        ),
        migrations.AddField(
            model_name='rgb',
            name='B',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rgb',
            name='G',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rgb',
            name='R',
            field=models.IntegerField(null=True),
        ),
    ]
