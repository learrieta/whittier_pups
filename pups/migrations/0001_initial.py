# Generated by Django 4.1.4 on 2023-04-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BabyDogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('quick_description', models.TextField(blank=True, null=True)),
                ('feature_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('page_picture1', models.ImageField(blank=True, null=True, upload_to='')),
                ('page_picture2', models.ImageField(blank=True, null=True, upload_to='')),
                ('page_picture3', models.ImageField(blank=True, null=True, upload_to='')),
                ('page_picture4', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
