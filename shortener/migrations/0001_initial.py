# Generated by Django 4.1.5 on 2023-01-18 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Url",
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
                ("link", models.URLField(max_length=10000)),
                ("uuid", models.CharField(max_length=10)),
            ],
        ),
    ]
