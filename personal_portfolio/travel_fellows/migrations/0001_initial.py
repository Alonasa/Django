# Generated by Django 5.0.6 on 2024-07-15 10:41

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=120)),
                ("surname", models.CharField(max_length=120)),
                ("username", models.EmailField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=120)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserPlans",
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
                (
                    "destinations",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "plans",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000),
                        default=list,
                        size=None,
                    ),
                ),
                ("companions", models.IntegerField(default=1)),
                ("dates_start", models.DateField()),
                ("dates_end", models.DateField()),
                ("kids", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "photo",
                    models.ImageField(blank=True, upload_to="travel_fellows/profile"),
                ),
                (
                    "hashtags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=300),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "destinations",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200),
                        default=list,
                        size=None,
                    ),
                ),
                ("level", models.IntegerField(default=1)),
                ("likes_count", models.IntegerField(default=0)),
                (
                    "hobbies",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=300),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "music",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=300),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "food",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=300),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "transport",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AV", "Avia"),
                            ("AU", "Automobile"),
                            ("BI", "Bicycle"),
                            ("HI", "Hiking"),
                        ],
                        default="AU",
                        max_length=2,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
