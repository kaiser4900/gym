# Generated by Django 3.2.7 on 2021-12-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niveles',
            name='name_nivel',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]