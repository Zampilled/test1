# Generated by Django 3.2.9 on 2022-03-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0020_auto_20220228_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]