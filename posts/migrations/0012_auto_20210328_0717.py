# Generated by Django 3.1.7 on 2021-03-28 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]