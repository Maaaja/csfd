# Generated by Django 3.0.2 on 2020-03-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csfd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmy',
            name='tvurci',
            field=models.ManyToManyField(to='csfd.Tvurci'),
        ),
    ]