# Generated by Django 4.2.6 on 2023-11-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_historypost_alter_eventpost_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historypost',
            options={'ordering': ('-id',), 'verbose_name': 'Исторический пост', 'verbose_name_plural': 'Исторические посты'},
        ),
        migrations.AddField(
            model_name='historypost',
            name='body',
            field=models.TextField(default=' ', verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historypost',
            name='centuary',
            field=models.PositiveIntegerField(default=21, verbose_name='Век'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historypost',
            name='title',
            field=models.CharField(default=' ', max_length=200, verbose_name='Тайтл'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historypost',
            name='year',
            field=models.PositiveIntegerField(default=0, verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='working_time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Время работы(конец)'),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='working_time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Время работы(начало)'),
        ),
    ]
