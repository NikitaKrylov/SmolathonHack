from django.db import models
from django.utils.translation import gettext_lazy as _
from posts.models import EventPost, HistoryPost


class ImageFile(models.Model):
    file = models.ImageField(_("Файл"), upload_to='posts')
    history_post = models.ForeignKey(HistoryPost, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    event_post = models.ForeignKey(EventPost, on_delete=models.CASCADE, related_name='images', blank=True, null=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Файл id {self.pk} - {self.file.name}"
