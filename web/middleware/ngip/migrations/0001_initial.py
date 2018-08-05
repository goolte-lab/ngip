# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 13:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0008_alter_user_username_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
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
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Account",
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
                (
                    "date_created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="Created On"
                    ),
                ),
                (
                    "date_modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="Modified On"
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[("a", "Active"), ("i", "Inactive"), ("p", "Paused")],
                        max_length=1,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date_modified", "-date_created"],
                "get_latest_by": "date_modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ping",
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
                ("name", models.CharField(max_length=255)),
                (
                    "date_received",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Last Received"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("a", "Active"), ("i", "Inactive"), ("p", "Paused")],
                        max_length=1,
                    ),
                ),
                ("notified", models.BooleanField(default=False)),
                (
                    "account",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ngip.Account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PingHistory",
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
                ("date_received", models.DateTimeField(verbose_name="Received On")),
                (
                    "ping",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ngip.Ping"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PingIntValue",
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
                ("key", models.CharField(max_length=255)),
                ("value", models.IntegerField(blank=True, null=True)),
                (
                    "compare",
                    models.CharField(
                        choices=[
                            ("eq", "Equal"),
                            ("ne", "Not Equal"),
                            ("z", "Blank"),
                            ("n", "Not Blank"),
                            ("gt", ">"),
                            ("ge", ">="),
                            ("lt", "<"),
                            ("le", "<="),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "ping",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ngip.Ping"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PingStringValue",
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
                ("key", models.CharField(max_length=255)),
                ("value", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "compare",
                    models.CharField(
                        choices=[
                            ("eq", "Equal"),
                            ("ne", "Not Equal"),
                            ("z", "Blank"),
                            ("n", "Not Blank"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "ping",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ngip.Ping"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PingToken",
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
                (
                    "date_created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="Created On"
                    ),
                ),
                (
                    "date_modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="Modified On"
                    ),
                ),
                ("token", models.CharField(max_length=255)),
                (
                    "date_last_used",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Last Used"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "ping",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ngip.Ping"
                    ),
                ),
            ],
            options={
                "ordering": ["-date_modified", "-date_created"],
                "get_latest_by": "date_modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserLoginToken",
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
                ("token", models.CharField(max_length=255)),
                (
                    "date_create",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="Created On"
                    ),
                ),
                ("date_login", models.DateTimeField(verbose_name="Login On")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="account",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ngip.Account",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Permission",
                verbose_name="user permissions",
            ),
        ),
    ]
