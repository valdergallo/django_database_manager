# Generated by Django 3.1.3 on 2020-11-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0002_servergroup"),
    ]

    operations = [
        migrations.AddField(
            model_name="server",
            name="backup_dir",
            field=models.CharField(default="/backups/", max_length=100),
        ),
    ]
