# Generated by Django 3.2.8 on 2021-10-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_venue_map_marker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='map_marker',
            field=models.CharField(max_length=1),
        ),
    ]
