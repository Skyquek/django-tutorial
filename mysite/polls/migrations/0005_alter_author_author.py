# Generated by Django 4.1.4 on 2022-12-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_author_author_name_alter_author_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="polls.question"
            ),
        ),
    ]
