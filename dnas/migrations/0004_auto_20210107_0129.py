# Generated by Django 3.1.5 on 2021-01-07 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnas', '0003_auto_20210106_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organism',
            old_name='mutations',
            new_name='mutation',
        ),
    ]