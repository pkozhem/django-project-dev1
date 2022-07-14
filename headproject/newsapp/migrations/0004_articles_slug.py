# Generated by Django 4.0.6 on 2022-07-14 11:39

import autoslug.fields
from django.db import migrations
import newsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_articles_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from=newsapp.models.Articles.instance),
        ),
    ]