# Generated by Django 4.1.7 on 2023-02-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=700)),
                ('message', models.TextField()),
            ],
        ),
    ]
