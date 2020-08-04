# Generated by Django 3.0.5 on 2020-08-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('poster', models.ImageField(max_length=1500, upload_to='movie_images/')),
                ('year', models.IntegerField()),
                ('length', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=50)),
                ('rating_votes', models.CharField(max_length=50)),
                ('plot', models.CharField(max_length=500)),
                ('trailer_id', models.CharField(max_length=50)),
                ('video_link', models.FileField(null=True, upload_to='movie_video/', verbose_name='')),
            ],
        ),
    ]
