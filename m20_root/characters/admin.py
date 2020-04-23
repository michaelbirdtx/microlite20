from django.contrib import admin
from .models import Class, Race, Weapon, Armor, Gear, Clothing, Character

# Register your models here.


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cost', 'damage', 'range')
    list_filter = ('type',)
    search_fields = ['name']


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cost', 'ac_bonus')
    list_filter = ('type',)
    search_fields = ['name']


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ['name']


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ['name']


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('armor', 'weapons', 'gear')
    list_display = ('name', 'race', 'character_class')
    list_filter = ('character_class', 'race')
    save_as = True
    search_fields = ['name']

    fieldsets = [
        (
            'CHARACTER DEFINITION', {
                'fields': [
                    'name',
                    ('race', 'character_class'),
                    ('level', 'xp'),
                    ('armor_class', 'hit_points'),
                    'slug',
                    'notes'
                ]
            }
        ),
        (
            'STATS', {
                'fields': [
                    ('str', 'dex', 'mind')
                ]
            }
        ),
        (
            'SKILLS', {
                'fields': [
                    ('phys', 'sub', 'know', 'com')
                ]
            }
        ),
        (
            'ATTACK BONUSES', {
                'fields': [
                    ('melee_bonus', 'ranged_bonus', 'magic_bonus')
                ]
            }
        ),
        (
            'INVENTORY', {
                'fields': [
                    ('copper', 'silver', 'gold', 'platinum'),
                    'clothing',
                    'armor',
                    'weapons',
                    'gear'
                ]
            }
        )
    ]
