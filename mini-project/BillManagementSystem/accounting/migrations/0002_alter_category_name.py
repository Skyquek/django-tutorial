# Generated by Django 4.1.6 on 2023-02-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.TextField(max_length=50, unique=True),
        ),
    ]
