# Generated by Django 3.2.12 on 2022-05-27 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_name_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='name',
        ),
    ]
