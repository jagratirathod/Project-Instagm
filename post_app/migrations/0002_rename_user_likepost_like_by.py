# Generated by Django 4.2.2 on 2023-07-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likepost',
            old_name='user',
            new_name='like_by',
        ),
    ]
