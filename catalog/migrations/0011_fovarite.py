# Generated by Django 3.0.4 on 2020-03-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200319_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fovarite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fovarites', models.ManyToManyField(blank=True, related_name='fovarit', to='catalog.Product')),
            ],
        ),
    ]
