# Generated by Django 3.1.5 on 2021-01-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dna',
            name='mutations',
            field=models.BooleanField(default=False),
        ),
    ]
