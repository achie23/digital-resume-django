# Generated by Django 3.2.12 on 2022-05-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_skill_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]