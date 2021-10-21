from typing import Type
from django.db import models
import uuid

from django.db.models.deletion import SET_NULL
from apps.user.models import User
from django.core.mail import send_mail
from django.core.validators import RegexValidator, FileExtensionValidator
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from re import T


class Attack(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('攻撃力パターン')
        verbose_name_plural = _('攻撃力パターン')

    Name = models.CharField(
        verbose_name=_('パターン名'),
        max_length=1024,
        blank=False,
    )

    Lv50Atk = models.IntegerField(
        verbose_name=_('★1攻撃力'),
        blank=True,
        default=0
    )

    Lv55Atk = models.IntegerField(
        verbose_name=_('★2攻撃力'),
        blank=True,
        default=0
    )

    Lv60Atk = models.IntegerField(
        verbose_name=_('★3攻撃力'),
        blank=True,
        default=0
    )

    Lv65Atk = models.IntegerField(
        verbose_name=_('★4攻撃力'),
        blank=True,
        default=0
    )

    Lv70Atk = models.IntegerField(
        verbose_name=_('★5攻撃力'),
        blank=True,
        default=0
    )

    Lv75Atk = models.IntegerField(
        verbose_name=_('★6攻撃力'),
        blank=True,
        default=0
    )

    Lv80Atk = models.IntegerField(
        verbose_name=_('★7攻撃力'),
        blank=True,
        default=0
    )

    Lv85Atk = models.IntegerField(
        verbose_name=_('★8攻撃力'),
        blank=True,
        default=0
    )

    Lv90Atk = models.IntegerField(
        verbose_name=_('★9攻撃力'),
        blank=True,
        default=0
    )

    Lv95Atk = models.IntegerField(
        verbose_name=_('★10攻撃力'),
        blank=True,
        default=0
    )

    Lv100Atk = models.IntegerField(
        verbose_name=_('★11攻撃力'),
        blank=True,
        default=0
    )


class SkillCondition(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('スキル条件')
        verbose_name_plural = _('スキル条件')

    Name = models.CharField(
        verbose_name=_('条件名'),
        max_length=1024,
        blank=False,
    )


class SkillEffect(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('スキル効果')
        verbose_name_plural = _('スキル効果')

    Name = models.CharField(
        verbose_name=_('効果名'),
        max_length=1024,
        blank=False,
    )


class Skill(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('スキル')
        verbose_name_plural = _('スキル')

    Name = models.CharField(
        verbose_name=_('スキル名(判別用)'),
        max_length=1024,
    )

    SKILLTYPE_CHOICES = (
        (0, "未選択"),
        (1, "ATTACK"),
        (2, "BOOST"),
        (3, "ASSIST"),
        (4, "GUARD"),
    )
    Type = models.IntegerField(
        verbose_name=_('スキル種別'),
        default=0,
        choices=SKILLTYPE_CHOICES,
    )

    SkillName = models.CharField(
        verbose_name=_('スキル名'),
        max_length=256,
        default="",
        blank=True,
    )

    SkillText = models.TextField(
        verbose_name=_('スキル効果テキスト'),
        default="",
        blank=True
    )

    SkillName2 = models.CharField(
        verbose_name=_('超開花スキル名'),
        max_length=256,
        default="",
        blank=True
    )

    SkillText2 = models.TextField(
        verbose_name=_('超開花スキル効果テキスト'),
        default="",
        blank=True
    )

    SkillConditionA = models.ForeignKey(
        SkillCondition,
        related_name='skillA_list',
        on_delete=models.PROTECT,
        verbose_name=_('スキル効果1条件'),
        blank=True,
        null=True
    )

    SkillEffectA = models.ForeignKey(
        SkillEffect,
        on_delete=models.PROTECT,
        related_name='skillA_list',
        verbose_name=_('スキル効果1'),
        blank=True,
        null=True
    )

    SkillParamA = models.IntegerField(
        verbose_name=_('スキル効果1効果値'),
        default=0,
    )

    SkillParamA2 = models.IntegerField(
        verbose_name=_('スキル効果1超開花効果値'),
        default=0,
    )

    SkillConditionB = models.ForeignKey(
        SkillCondition,
        related_name='skillB_list',
        on_delete=models.PROTECT,
        verbose_name=_('スキル効果2条件'),
        blank=True,
        null=True
    )

    SkillEffectB = models.ForeignKey(
        SkillEffect,
        on_delete=models.PROTECT,
        related_name='skillB_list',
        verbose_name=_('スキル効果2'),
        blank=True,
        null=True
    )

    SkillParamB = models.IntegerField(
        verbose_name=_('スキル効果2効果値'),
        default=0,
    )

    SkillParamB2 = models.IntegerField(
        verbose_name=_('スキル効果2超開花効果値'),
        default=0,
    )


class Work(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('作品')
        verbose_name_plural = _('作品')

    Name = models.CharField(
        verbose_name=_('作品名'),
        max_length=1024,
        blank=False,
    )


class Character(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('キャラクター')
        verbose_name_plural = _('キャラクター')

    Name = models.CharField(
        verbose_name=_('キャラクター名'),
        max_length=1024,
        blank=False,
    )

    Work = models.ForeignKey(
        Work,
        on_delete=models.PROTECT,
        verbose_name=_('作品'),
        null=True
    )


class Card(models.Model):
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('カード')
        verbose_name_plural = _('カード')

    Name = models.CharField(
        verbose_name=_('カード名'),
        max_length=1024,
        blank=False,
    )

    Number = models.CharField(
        verbose_name=_('カード番号'),
        max_length=64,
        blank=True,
    )

    RARE_CHOICES = (
        (0, "未選択"),
        (1, "N"),
        (2, "R"),
        (3, "SR"),
        (4, "SR+"),
        (5, "SSR"),
    )
    Rare = models.IntegerField(
        verbose_name=_('レアリティ'),
        default=0,
        choices=RARE_CHOICES,
    )

    TYPE_CHOICES = (
        (0, "未選択"),
        (1, "FIRE"),
        (2, "AQUA"),
        (3, "LEAF")
    )
    Type = models.IntegerField(
        verbose_name=_('属性'),
        default=0,
        choices=TYPE_CHOICES,
    )

    Date = models.DateField(
        verbose_name=_('追加日'),
        blank=True,
        null=True
    )

    Character = models.ForeignKey(
        Character,
        on_delete=models.PROTECT,
        verbose_name=_('作品'),
        null=True,
        blank=True
    )

    Atk = models.ForeignKey(
        Attack,
        on_delete=models.PROTECT,
        verbose_name=_('攻撃力パターン'),
        null=True,
        blank=True
    )

    Skill = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        verbose_name=_('スキル'),
        null=True,
        blank=True
    )

    HowToGet = models.CharField(
        verbose_name=_('入手方法'),
        max_length=256,
        blank=True
    )

    HowToGet2 = models.TextField(
        verbose_name=_('入手方法詳細'),
        max_length=256,
        blank=True
    )
