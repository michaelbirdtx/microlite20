from django.db import models
import uuid

# Create your models here.


class Class(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Classes'
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Race(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(blank=True)
    skill_bonus = models.IntegerField('Skill Bonus', default=0)
    str_bonus = models.IntegerField('STR Bonus', default=0)
    dex_bonus = models.IntegerField('DEX Bonus', default=0)
    mind_bonus = models.IntegerField('MIND Bonus', default=0)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    WEAPON_TYPE = (
        ('L', 'Light'),
        ('1H', 'One-Handed'),
        ('2H', 'Two-Handed'),
        ('R', 'Ranged'),
    )
    type = models.CharField(max_length=10, choices=WEAPON_TYPE)
    cost = models.CharField(max_length=10, blank=False, default='-')
    damage = models.CharField(max_length=10, blank=False, default='-')
    range = models.CharField(max_length=10, blank=False, default='-')

    def __str__(self):
        return self.name


class Armor(models.Model):
    class Meta:
        ordering = ['type', 'name']
        verbose_name_plural = 'Armor'
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    ARMOR_TYPE = (
        ('L', 'Light'),
        ('M', 'Medium'),
        ('H', 'Heavy'),
        ('S', 'Shield'),
    )
    type = models.CharField(max_length=10, choices=ARMOR_TYPE)
    cost = models.CharField(max_length=10, blank=False, default='-')
    ac_bonus = models.IntegerField('AC Bonus', default=1)

    def __str__(self):
        return self.name


class Gear(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Gear'
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    cost = models.CharField(max_length=10, blank=False, default='-')

    def __str__(self):
        return self.name


class Character(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=uuid.uuid4)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    character_class = models.ForeignKey(Class, on_delete=models.PROTECT)
    level = models.IntegerField(default=1)
    hit_points = models.IntegerField(default=1)
    xp = models.IntegerField('XP', default=0)
    str = models.IntegerField('STR', default=10)
    dex = models.IntegerField('DEX', default=10)
    mind = models.IntegerField('MIND', default=10)
    phys = models.IntegerField('phys', default=0)
    sub = models.IntegerField(default=0)
    know = models.IntegerField(default=0)
    com = models.IntegerField(default=0)
    melee_bonus = models.IntegerField('Melee attack bonus', default=0)
    ranged_bonus = models.IntegerField('Ranged attack bonus', default=0)
    magic_bonus = models.IntegerField('Magic attack bonus', default=0)
    armor = models.ManyToManyField(Armor, blank=True)
    armor_class = models.IntegerField(default=10)
    weapons = models.ManyToManyField(Weapon, blank=True)
    gear = models.ManyToManyField(Gear, blank=True)
    copper = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    platinum = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name