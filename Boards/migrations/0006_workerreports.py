# Generated by Django 4.2 on 2023-05-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boards', '0005_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='workerreports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('NumberPhone', models.CharField(max_length=50)),
                ('Discrbition', models.TextField()),
            ],
        ),
    ]
