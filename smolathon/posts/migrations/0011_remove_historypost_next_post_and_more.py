# Generated by Django 4.2.6 on 2023-11-09 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_historypost_options_historypost_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historypost',
            name='next_post',
        ),
        migrations.AddField(
            model_name='historypost',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_post', to='posts.historypost', verbose_name='Предыдущий пост'),
        ),
    ]
