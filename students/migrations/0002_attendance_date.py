# Generated by Django 3.2.6 on 2021-08-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]