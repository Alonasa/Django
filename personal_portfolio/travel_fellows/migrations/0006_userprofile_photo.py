# Generated by Django 5.0.6 on 2024-06-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "travel_fellows",
            "0005_alter_user_email_alter_user_name_alter_user_password_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="photo",
            field=models.FilePathField(default="photos/default.jpg"),
        ),
    ]
