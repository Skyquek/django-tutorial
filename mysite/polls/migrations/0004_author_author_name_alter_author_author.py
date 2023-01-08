# Generated by Django 4.1.4 on 2022-12-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="author_name",
            field=models.CharField(default="ali", max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="author",
            name="author",
            field=models.ForeignKey(
                default="Ali",
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.question",
            ),
        ),
    ]