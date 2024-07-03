# Generated by Django 5.0.4 on 2024-04-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_profile_accept_profile_male'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Полный пакет'), ('free', 'Бесплатный пакет')], default='free', max_length=30),
        ),
    ]
