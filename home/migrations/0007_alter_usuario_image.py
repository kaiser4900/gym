# Generated by Django 3.2.7 on 2021-12-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_usuario_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(null=True, upload_to='static/assets/img/profile/'),
        ),
    ]
