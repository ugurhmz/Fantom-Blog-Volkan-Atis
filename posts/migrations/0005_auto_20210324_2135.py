# Generated by Django 3.1.7 on 2021-03-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210324_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', editable=False),
        ),
    ]
