# Generated by Django 4.1.4 on 2023-04-20 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pups', '0002_babydogs_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='babydogs',
            old_name='quick_description',
            new_name='what_includes',
        ),
    ]
