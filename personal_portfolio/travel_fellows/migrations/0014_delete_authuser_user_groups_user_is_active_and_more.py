# Generated by Django 5.0.6 on 2024-07-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("travel_fellows", "0013_rename_username_authuser_email"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AuthUser",
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                related_name="travel_fellows_user_groups", to="auth.group"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                related_name="travel_fellows_user_permissions", to="auth.permission"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
