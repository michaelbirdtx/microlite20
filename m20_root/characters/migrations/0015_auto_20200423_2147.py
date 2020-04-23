# Generated by Django 3.0.5 on 2020-04-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_auto_20200423_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='special_ability',
        ),
        migrations.RemoveField(
            model_name='race',
            name='special_ability',
        ),
        migrations.AddField(
            model_name='race',
            name='skill_roll_bonus',
            field=models.IntegerField(default=0, verbose_name='Skill Roll Bonus'),
        ),
    ]
