# Generated by Django 4.1.3 on 2023-09-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("haji_salam", "0037_alter_property_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="city",
            field=models.CharField(
                choices=[
                    ("erbil", "erbil"),
                    ("sulaymaniah", "sulaymaniah"),
                    ("duhok", "duhok"),
                ],
                max_length=35,
            ),
        ),
    ]
