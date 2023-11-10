import uuid
from enum import Enum

from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from account.utils.check_in_place import create_qr_code


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
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    post = models.OneToOneField(EventPost, on_delete=models.CASCADE, related_name='test')
    qr_code = models.ImageField(_("QR код"), blank=True, upload_to='qrcodes/')

    @property
    def build_url(self):
        return 'http://misis52.itatmisis.ru' + reverse('event_post_test', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.qr_code: return

        file_name = str(self.id) + ".png"
        file_path = create_qr_code(self.build_url, file_name)

        with NamedTemporaryFile() as temp_file:
            with open(file_path, 'rb') as file:
                temp_file.write(file.read())

            self.qr_code.save(file_name, File(temp_file), save=True)

        default_storage.delete(file_path)

    def get_absolute_url(self):
        return reverse('event_post_test', kwargs={'id': self.id})


class TestQuestion(models.Model):
    test = models.ForeignKey(PlaceTest, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=300)


class QuestionAnswer(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField(default=False)


class PlaceTestResult(models.Model):
    user = models.ForeignKey(User, related_name='test_results', on_delete=models.SET_NULL, null=True, blank=True)
    result_points = models.PositiveIntegerField()
    test = models.ForeignKey(PlaceTest, on_delete=models.SET_NULL, null=True, blank=True)

