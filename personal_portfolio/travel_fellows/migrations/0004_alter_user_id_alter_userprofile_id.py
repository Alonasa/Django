# Generated by Django 5.0.6 on 2024-06-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("travel_fellows", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
