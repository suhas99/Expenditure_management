# Generated by Django 2.1.4 on 2019-10-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enamour', '0016_auto_20191017_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='expendtituredetails',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
