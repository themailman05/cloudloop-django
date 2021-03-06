# Generated by Django 3.0.5 on 2020-04-25 10:30

import cloudloop.helper
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(default=cloudloop.helper.create_hash, max_length=32, unique=True)),
                ('timestamp', models.IntegerField(default=cloudloop.helper.time_stamp)),
                ('beats', models.IntegerField()),
                ('sample_rate', models.IntegerField(choices=[(44100, '44.1Khz'), (48000, '48Khz'), (96000, '96Khz')])),
                ('bit_depth', models.IntegerField(choices=[(24, '24 bit'), (16, '16 bit')])),
                ('channels', models.IntegerField(choices=[(1, 'mono'), (2, 'stereo')])),
                ('frame_count', models.IntegerField()),
                ('wav_link', models.URLField(unique=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(default=cloudloop.helper.create_hash, max_length=32, unique=True)),
                ('title', models.CharField(max_length=64)),
                ('timestamp', models.IntegerField(default=cloudloop.helper.time_stamp)),
                ('clients', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('loops', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loops_set', to='looper.Loop')),
            ],
        ),
        migrations.AddField(
            model_name='loop',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='looper.Session'),
        ),
    ]
