# Generated by Django 4.1.7 on 2023-05-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boards', '0009_worker_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('arrivalDateTimeAway', models.DateTimeField()),
                ('departureDateTimeA', models.DateTimeField()),
                ('durationInMinutesA', models.IntegerField()),
                ('away', models.CharField(max_length=1000)),
                ('awayimg', models.ImageField(upload_to='')),
                ('arrivalDateTimeR', models.DateTimeField()),
                ('departureDateTimeR', models.DateTimeField()),
                ('durationInMinutesR', models.IntegerField()),
                ('returnf', models.CharField(max_length=1000)),
                ('returnimg', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
