# Generated by Django 4.0.3 on 2022-04-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_startup_startup_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='iitian',
            field=models.BooleanField(null=True),
        ),
    ]
