# Generated by Django 3.2.7 on 2021-12-09 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_usuario_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(upload_to='static/assets/img/profile/'),
        ),
    ]
