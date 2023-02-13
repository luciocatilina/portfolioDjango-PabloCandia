# Generated by Django 4.1 on 2023-02-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('repository', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('functionalities', models.CharField(max_length=300)),
                ('used_tools', models.CharField(max_length=300)),
                ('git_page', models.CharField(blank=True, max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img_proyect')),
            ],
        ),
    ]
