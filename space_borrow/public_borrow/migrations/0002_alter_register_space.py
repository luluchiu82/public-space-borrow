# Generated by Django 5.0 on 2024-02-19 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_borrow", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="space",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="public_borrow.space"
            ),
        ),
    ]
