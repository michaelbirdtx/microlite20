# Generated by Django 3.2.7 on 2021-09-18 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20210918_0429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charactergear',
            options={'ordering': ['gear__name'], 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='gear',
            options={'ordering': ['name'], 'verbose_name': 'Item', 'verbose_name_plural': 'Item'},
        ),
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='characters.class', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='charactergear',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.gear', verbose_name='Item'),
        ),
    ]