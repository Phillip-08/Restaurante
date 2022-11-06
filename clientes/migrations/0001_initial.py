# Generated by Django 4.1.1 on 2022-11-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("codigo", models.CharField(blank=True, max_length=200, null=True)),
                ("nombre", models.CharField(blank=True, max_length=200, null=True)),
                ("telefono", models.CharField(blank=True, max_length=200, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]