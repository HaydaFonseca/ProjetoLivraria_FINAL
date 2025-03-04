# Generated by Django 5.1.5 on 2025-02-02 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_livro_autores"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
