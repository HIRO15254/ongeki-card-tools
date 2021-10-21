from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Attack, SkillCondition, SkillEffect, Skill, Work, Character, Card


class MyAttackAdmin(ModelAdmin):
    fieldsets = (
        ('名前', {'fields': ('Name',)}),
        ('数値', {'fields': ('Lv50Atk', 'Lv55Atk', 'Lv60Atk', 'Lv65Atk', 'Lv70Atk', 'Lv75Atk', 'Lv80Atk', 'Lv85Atk', 'Lv90Atk', 'Lv95Atk', 'Lv100Atk')}),
    )

    list_display = ('Name', 'Lv50Atk', 'Lv55Atk', 'Lv60Atk', 'Lv65Atk', 'Lv70Atk',)
    search_fields = ('Name',)
    list_editable = ('Lv50Atk', 'Lv55Atk', 'Lv60Atk', 'Lv65Atk', 'Lv70Atk',)
    ordering = ('Lv70Atk', 'Lv65Atk', 'Lv60Atk')


class MySkillAdmin(ModelAdmin):
    fieldsets = (
        ('名前', {'fields': ('Name', 'SkillName', 'SkillName2', )}),
        ('説明', {'fields': ('SkillText', 'SkillText2',)}),
        ('効果1', {'fields': ('SkillConditionA', 'SkillEffectA', 'SkillParamA', 'SkillParamA2',)}),
        ('効果1', {'fields': ('SkillConditionB', 'SkillEffectB', 'SkillParamB', 'SkillParamB2',)}),
    )

    list_display = ('SkillName', 'SkillName2', 'SkillConditionA', 'SkillEffectA', 'SkillParamA', 'SkillParamA2', 'SkillConditionB', 'SkillEffectB', 'SkillParamB', 'SkillParamB2',)
    search_fields = ('SkillName',)
    list_editable = ('SkillConditionA', 'SkillEffectA', 'SkillParamA', 'SkillParamA2', 'SkillConditionB', 'SkillEffectB', 'SkillParamB', 'SkillParamB2',)


class MyCardAdmin(ModelAdmin):
    fieldsets = (
        ('名前', {'fields': ('Name',)}),
        ('基本情報', {'fields': ('Rare', 'Character', 'Date', 'Number',)}),
        ('バトル効果', {'fields': ('Type', 'Atk', 'Skill',)}),
        ('入手', {'fields': ('HowToGet', 'HowToGet2',)}),
    )
    list_display = ('Name', 'Rare', 'Character', 'Date', 'Number', 'Type', 'Atk', 'Skill', 'HowToGet', 'HowToGet2',)
    search_fields = ('SkillName',)
    list_editable = ('Rare', 'Character', 'Date', 'Number', 'Type', 'Atk', 'Skill', 'HowToGet',)


# Register your models here.
admin.site.register(Attack, MyAttackAdmin)
admin.site.register(SkillCondition)
admin.site.register(SkillEffect)
admin.site.register(Skill, MySkillAdmin)
admin.site.register(Work)
admin.site.register(Character)
admin.site.register(Card, MyCardAdmin)
