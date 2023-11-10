# Generated by Django 4.2.6 on 2023-11-02 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_culturepost_options_alter_eventpost_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='culturepost',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_post', to='posts.culturepost', verbose_name='Следующий пост'),
        ),
    ]