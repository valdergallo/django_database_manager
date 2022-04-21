# Generated by Django 3.1.3 on 2020-11-07 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("server", "0006_auto_20201107_1031"),
    ]

    operations = [
        migrations.AlterField(
            model_name="database",
            name="host",
            field=models.CharField(default="localhost", max_length=250),
        ),
        migrations.AlterField(
            model_name="server",
            name="databases",
            field=models.ManyToManyField(blank=True, to="server.Database"),
        ),
        migrations.AlterField(
            model_name="servergroup",
            name="servers",
            field=models.ManyToManyField(blank=True, to="server.Server"),
        ),
        migrations.CreateModel(
            name="UploadStorageConfig",
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
                    "storage_type",
                    models.CharField(
                        choices=[
                            ("AMS3", "Amazon S3"),
                            ("ACLD", "Apache Libcloud"),
                            ("ASTG", "Azure Storage"),
                            ("DGON", "Digital Ocean"),
                            ("DRPB", "Dropbox"),
                            ("FTP", "Ftp"),
                            ("GCTG", "Google Cloud Storage"),
                            ("SFTP", "Sftp"),
                        ],
                        max_length=5,
                    ),
                ),
                ("config_vars", models.TextField(max_length=500)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="database",
            name="storage_type",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="server.uploadstorageconfig",
            ),
        ),
    ]
