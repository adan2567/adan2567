# Generated by Django 4.2.11 on 2025-02-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='a.pr', upload_to='upload')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
