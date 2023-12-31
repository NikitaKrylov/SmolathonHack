# Generated by Django 4.2.6 on 2023-11-09 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediacore', '0003_remove_imagefile_culture_post'),
        ('posts', '0008_alter_culturepost_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_post', to='posts.historypost', verbose_name='Следующий пост')),
            ],
            options={
                'verbose_name': 'Исторический пост',
                'verbose_name_plural': 'Исторические посты',
            },
        ),
        migrations.AlterModelOptions(
            name='eventpost',
            options={'ordering': ('-id',), 'verbose_name': 'Пост события', 'verbose_name_plural': 'Посты событий'},
        ),
        migrations.DeleteModel(
            name='CulturePost',
        ),
    ]
