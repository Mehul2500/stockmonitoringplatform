# Generated by Django 4.2.1 on 2023-05-20 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "stock_monitoring",
            "0002_stock_remove_watchlist_symbol_alter_watchlist_user_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Symbol",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="watchlist",
            name="stocks",
        ),
        migrations.AlterField(
            model_name="watchlist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="symbols",
            field=models.ManyToManyField(to="stock_monitoring.symbol"),
        ),
    ]
