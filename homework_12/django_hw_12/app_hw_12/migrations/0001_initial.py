# Generated by Django 3.1.6 on 2021-02-01 20:26

import app_hw_12.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Homework",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hw_text", models.CharField(max_length=200)),
                ("deadline", models.FloatField()),
                ("created", models.IntegerField(null=True)),
                ("answer", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            bases=(app_hw_12.models.Programmist, models.Model),
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            bases=(app_hw_12.models.Programmist, models.Model),
        ),
    ]
