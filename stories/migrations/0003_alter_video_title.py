# Generated by Django 4.0.6 on 2022-08-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=5000),
        ),
    ]
