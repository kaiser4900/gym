# Generated by Django 3.2.7 on 2021-12-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niveles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
