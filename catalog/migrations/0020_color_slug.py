# Generated by Django 2.2.10 on 2020-08-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20200801_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
