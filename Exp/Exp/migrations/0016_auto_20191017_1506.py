# Generated by Django 2.1.4 on 2019-10-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enamour', '0015_expendtituredetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expendtituredetails',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
