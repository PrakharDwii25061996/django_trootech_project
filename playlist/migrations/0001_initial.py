# Generated by Django 5.0.6 on 2024-06-20 09:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('tracks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_tracks', to='admin_panel.track')),
            ],
        ),
    ]
