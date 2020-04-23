# Generated by Django 3.0.5 on 2020-04-23 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20200423_0324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armor',
            options={'ordering': ['type', 'name'], 'verbose_name_plural': 'Armor'},
        ),
        migrations.AlterField(
            model_name='armor',
            name='type',
            field=models.CharField(choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy'), ('S', 'Shield')], max_length=10),
        ),
    ]