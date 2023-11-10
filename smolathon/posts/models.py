from enum import Enum

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Categories(Enum):
    FOOD = "Питание"
    LEISURE = "Досуг"
    OTHER = "Другое"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value_from_string(cls, text: str):
        for item in cls:
            if item.name == text.strip():
                return Categories(item.name)
        return Categories.OTHER.value


class Subcategories(Enum):
    MUSEUMS = "Музеи"
    CINEMAS = "Кинотеатры"
    CAFFE = "Кафе"
    SHOPPING_CENTERS = "Торгово-развлекательные центры"
    RESTAURANTS = "Рестораны"
    ACTIVE_LEISURE = "Активный отдых"
    BARS = "Бары"
    CONCERT_HALLS = "Концертные и выставочные залы"
    THEATERS = "Театры"
    OTHER = "Другое"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value_from_string(cls, text: str):
        for item in cls:
            if item.name == text.strip():
                return Subcategories(item.name)
        return Subcategories.OTHER.value


class EventPost(models.Model):

    class Meta:
        verbose_name = "Пост события"
        verbose_name_plural = "Посты событий"
        ordering = ('-id',)

    title = models.CharField(_('Заголовок'), max_length=100)
    description = models.TextField(_('Описание'), max_length=400, default='', blank=True)

    address = models.CharField(_("Адррес"), max_length=100)

    category = models.CharField(_("Категория"), max_length=100, default='')
    subcategory = models.CharField(_("Вторичная категория"), max_length=100, default='')

    phone = models.CharField(_("Номер телефона"), default='', max_length=50)
    site = models.URLField(_("Вебсайт"), blank=True, null=True)

    is_unlimited_working_time = models.BooleanField(_("Время работы неограничено"), default=True)
    working_time_start = models.TimeField(_("Время работы(начало)"), blank=True, null=True)
    working_time_end = models.TimeField("Время работы(конец)", blank=True, null=True)

    is_unlimited_event_time = models.BooleanField(_("Время проведения неограничено"), default=True)
    event_time_start = models.DateTimeField(_("Период проведения(начало)"), blank=True, null=True)
    event_time_end = models.DateTimeField(_("Период проведения(конец)"), blank=True, null=True)

    def get_absolute_url(self):
        return reverse('event_post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class HistoryPost(models.Model):
    title = models.CharField(_("Тайтл"), max_length=200)
    body = models.TextField(_("Текст"))
    year = models.PositiveIntegerField(_("Год"), default=0)
    century = models.PositiveIntegerField(_("Век"))

    previous_post = models.ForeignKey('posts.HistoryPost', on_delete=models.SET_NULL, verbose_name=_("Предыдущий пост"), related_name='next_post', blank=True, null=True)

    class Meta:
        verbose_name = "Исторический пост"
        verbose_name_plural = "Исторические посты"
        ordering = ('-id',)

    def get_absolute_url(self):
        return reverse('history_post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class PlaceTest(models.Model):
    event_post = models.ForeignKey(EventPost, on_delete=models.CASCADE)


class TestQuestion(models.Model):
    test = models.ForeignKey(PlaceTest, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)


