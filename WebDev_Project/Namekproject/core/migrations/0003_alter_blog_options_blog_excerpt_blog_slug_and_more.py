# Generated by Django 5.1.4 on 2025-03-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='blog',
            name='excerpt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blog_thumbnails/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
