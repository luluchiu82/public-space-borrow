# Generated by Django 4.1.4 on 2024-02-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_borrow', '0002_alter_register_space'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date',
            field=models.DateField(),
        ),
    ]
