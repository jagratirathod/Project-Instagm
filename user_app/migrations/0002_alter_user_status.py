# Generated by Django 4.2.2 on 2023-06-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Follow', 'follow'), ('Following', 'following'), ('requested', 'requested'), ('conform', 'conform'), ('delete', 'delete')], default='Follow', max_length=20, null=True),
        ),
    ]
