# Generated by Django 5.0.6 on 2024-06-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=10)),
                ('experience', models.TextField(max_length=300)),
                ('hobies', models.TextField(max_length=100)),
                ('languages', models.TextField(max_length=100)),
            ],
        ),
    ]
