# Generated by Django 5.0.6 on 2024-06-19 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Pre", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ThreeDModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model_file", models.FileField(upload_to="3d_models/")),
                ("description", models.TextField(blank=True, null=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "project",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="threedmodel",
                        to="Pre.project",
                    ),
                ),
            ],
        ),
    ]
