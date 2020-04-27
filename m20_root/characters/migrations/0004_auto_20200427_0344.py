# Generated by Django 3.0.5 on 2020-04-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20200427_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charactergear',
            options={'ordering': ['gear__name'], 'verbose_name': 'Adventuring Gear', 'verbose_name_plural': 'Adventuring Gear'},
        ),
        migrations.AddField(
            model_name='class',
            name='attack_bonus',
            field=models.IntegerField(default=0),
        ),
    ]
