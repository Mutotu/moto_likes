# Generated by Django 3.2.12 on 2022-03-11 11:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='likes/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motobook.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('like', models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('like_total', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('photo_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motobook.photo')),
                ('users', models.ManyToManyField(to='motobook.Profile')),
            ],
        ),
    ]
