# Generated by Django 4.0.3 on 2022-04-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_startup_hostel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='iitian',
            field=models.CharField(max_length=6, null=True),
        ),
    ]