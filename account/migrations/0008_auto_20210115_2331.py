# Generated by Django 3.1.3 on 2021-01-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210115_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(default='no-avatar.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]
