from django.db import models
from django.db.models import Sum
import uuid
import math

WEAPON_TYPE = (
    ('L', 'Light'),
    ('1H', 'One-Handed'),
    ('2H', 'Two-Handed'),
    ('R', 'Ranged'),
)

ARMOR_TYPE = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('H', 'Heavy'),
    ('S', 'Shield'),
)

# Create your models here.


class Class(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Classes'
    name = models.CharField(max_length=20)
    abilities = models.TextField(blank=True)
    phys_bonus = models.IntegerField(default=0)
    sub_bonus = models.IntegerField(default=0)
    know_bonus = models.IntegerField(default=0)
    com_bonus = models.IntegerField(default=0)
    light_armor = models.BooleanField(default=False)
    medium_armor = models.BooleanField(default=False)
    heavy_armor = models.BooleanField(default=False)
    shields = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Race(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=20)
    abilities = models.TextField(blank=True)
    skill_roll_bonus = models.IntegerField('Skill Roll Bonus', default=0)
    str_bonus = models.IntegerField('STR Bonus', default=0)
    dex_bonus = models.IntegerField('DEX Bonus', default=0)
    mind_bonus = models.IntegerField('MIND Bonus', default=0)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=WEAPON_TYPE)
    cost = models.CharField(max_length=10, blank=False, default='-')
    damage = models.CharField(max_length=10, blank=False, default='-')
    range = models.CharField(max_length=10, blank=False, default='-')

    def __str__(self):
        return self.name


class Armor(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Armor'
    name = models.CharField(max_length=50)
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
    cost = models.CharField(max_length=10, blank=False, default='-')

    def __str__(self):
        return self.name


class Clothing(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Clothing'
    name = models.CharField(max_length=50)
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
    hit_points_max = models.IntegerField('Max HP', default=1)
    xp = models.IntegerField('XP', default=0)
    str = models.IntegerField('STR', default=10)
    dex = models.IntegerField('DEX', default=10)
    mind = models.IntegerField('MIND', default=10)
    armor = models.ManyToManyField(Armor, blank=True)
    weapons = models.ManyToManyField(Weapon, blank=True)
    gear = models.ManyToManyField(
        Gear, blank=True, through='CharacterGear')
    clothing = models.ForeignKey(
        Clothing, blank=True, null=True, on_delete=models.PROTECT)
    copper = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    platinum = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    @property
    def armor_class(self):
        return (
            (10 + math.floor((self.dex - 10)/2)) +
            self.armor.all().aggregate(Sum('ac_bonus')).get('ac_bonus__sum')
        )

    @property
    def str_bonus(self):
        return math.floor((self.str - 10)/2)

    @property
    def dex_bonus(self):
        return math.floor((self.dex - 10)/2)

    @property
    def mind_bonus(self):
        return math.floor((self.mind - 10)/2)

    @property
    def phys(self):
        return self.level + self.character_class.phys_bonus

    @property
    def sub(self):
        return self.level + self.character_class.sub_bonus

    @property
    def know(self):
        return self.level + self.character_class.know_bonus

    @property
    def com(self):
        return self.level + self.character_class.com_bonus

    @property
    def melee_bonus(self):
        return self.level + math.floor((self.str - 10)/2)

    @property
    def ranged_bonus(self):
        return self.level + math.floor((self.dex - 10)/2)

    @property
    def magic_bonus(self):
        return self.level + math.floor((self.mind - 10)/2)

    def get_absolute_url(self):
        return "/characters/%s" % self.slug

    def __str__(self):
        return self.name


class CharacterGear(models.Model):
    class Meta:
        verbose_name = 'Adventuring Gear'
        verbose_name_plural = 'Adventuring Gear'
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.gear.name
