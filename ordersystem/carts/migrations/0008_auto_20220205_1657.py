# Generated by Django 3.2.9 on 2022-02-05 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_auto_20220205_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_items',
        ),
        migrations.AddField(
            model_name='cart',
            name='order_items',
            field=models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='carts.cartitem'),
        ),
    ]