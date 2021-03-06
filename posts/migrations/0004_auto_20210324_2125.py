# Generated by Django 3.1.7 on 2021-03-24 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210324_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
