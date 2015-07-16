# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('popularity', models.FloatField()),
                ('imdb_score', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ForeignKey(related_name=b'genre', to='app.Movies'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='genre',
            unique_together=set([('movie', 'order')]),
        ),
    ]
