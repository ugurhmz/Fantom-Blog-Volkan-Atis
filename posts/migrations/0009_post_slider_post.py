# Generated by Django 3.1.7 on 2021-03-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210325_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slider_post',
            field=models.BooleanField(default=False),
        ),
    ]
