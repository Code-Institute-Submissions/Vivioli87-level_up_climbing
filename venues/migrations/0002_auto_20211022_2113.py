# Generated by Django 3.2.8 on 2021-10-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venue',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]
