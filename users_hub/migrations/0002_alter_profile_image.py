# Generated by Django 4.0.4 on 2022-04-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
