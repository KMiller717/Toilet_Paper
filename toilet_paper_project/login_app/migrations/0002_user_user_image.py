# Generated by Django 2.2.3 on 2020-03-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]
