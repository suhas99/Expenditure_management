# Generated by Django 2.1.4 on 2019-10-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enamour', '0013_auto_20191017_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_stats',
            name='amount',
            field=models.FloatField(max_length=10),
        ),
    ]
