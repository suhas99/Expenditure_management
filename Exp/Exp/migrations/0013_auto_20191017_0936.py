# Generated by Django 2.1.4 on 2019-10-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enamour', '0012_payment_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_stats',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]