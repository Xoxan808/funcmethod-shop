# Generated by Django 2.2.10 on 2020-05-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('0', 'Icra olunmayib'), ('1', 'Yoldadir'), ('2', 'Çatdırılıb'), ('3', 'Imtina edilib'), ('4', 'Qaytarilib')], default='0', max_length=100),
        ),
    ]
