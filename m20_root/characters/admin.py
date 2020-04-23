from django.contrib import admin
from .models import Class, Race, Weapon, Armor, Gear, Character

# Register your models here.


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cost', 'damage', 'range')
    list_filter = ('type',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cost', 'ac_bonus')
    list_filter = ('type',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('armor', 'weapons', 'gear')
    list_display = ('name', 'race', 'character_class')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
