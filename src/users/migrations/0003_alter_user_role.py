# Generated by Django 4.1.4 on 2023-01-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_managers_user_groups_user_is_superuser_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "Admin"), ("manager", "Manager"), ("user", "User")],
                max_length=7,
            ),
        ),
    ]
