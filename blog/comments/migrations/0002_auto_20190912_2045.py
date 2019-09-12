# Generated by Django 2.1.5 on 2019-09-12 12:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='belong_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Articles', verbose_name='属于那篇文章'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 12, 45, 13, 486829, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
