# Generated by Django 4.1.4 on 2023-03-26 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("productorder", "0007_alter_order_coupon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="productorder.ordercoupon",
            ),
        ),
    ]
