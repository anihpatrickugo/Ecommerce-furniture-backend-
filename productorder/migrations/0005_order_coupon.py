# Generated by Django 4.1.4 on 2023-03-26 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("productorder", "0004_ordercoupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="productorder.ordercoupon",
            ),
            preserve_default=False,
        ),
    ]
