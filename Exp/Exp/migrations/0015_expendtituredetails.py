# Generated by Django 2.1.4 on 2019-10-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enamour', '0014_auto_20191017_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='expendtitureDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(max_length=10)),
                ('Date', models.DateField()),
            ],
        ),
    ]
