# Generated by Django 3.2.8 on 2021-10-18 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0003_auto_20211017_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='profiles.userprofile'),
        ),
    ]
