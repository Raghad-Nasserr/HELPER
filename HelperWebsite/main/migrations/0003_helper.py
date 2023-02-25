# Generated by Django 4.1.7 on 2023-02-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_helprequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('description_of_experiences', models.TextField()),
                ('helper_cv', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
