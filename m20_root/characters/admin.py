from django.contrib import admin
from .models import (Player, Class, Race, Weapon, Armor, Gear,
                     Clothing, Character, CharacterGear, GearPack,
                     GearInPack)

admin.site.site_title = 'Microlite 20'
admin.site.site_header = 'Microlite 20'
admin.site.index_title = 'Administration'

# Models


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')
    search_fields = ('name', 'email')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'abilities')
    search_fields = ['name']


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'abilities')
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


class GearInPackInline(admin.TabularInline):
    model = GearInPack
    autocomplete_fields = ['gear']
    extra = 0
    fields = ('gear', 'quantity')
    verbose_name = 'Item'
    verbose_name_plural = 'Items'


@admin.register(GearPack)
class GearPackAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ['name']
    inlines = [
        GearInPackInline
    ]


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ['name']


class CharacterGearInline(admin.TabularInline):
    model = CharacterGear
    autocomplete_fields = ['gear']
    extra = 0
    fields = ('gear', 'quantity')
    verbose_name = 'Item'
    verbose_name_plural = 'Adventuring Gear'


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('armor', 'weapons', 'gear')
    inlines = [
        CharacterGearInline
    ]
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
                    'hit_points',
                    'slug',
                    'player',
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
            'INVENTORY', {
                'fields': [
                    ('copper', 'silver', 'gold', 'platinum'),
                    'clothing',
                    'armor',
                    'weapons'
                ]
            }
        )
    ]
