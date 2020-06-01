# Generated by Django 2.2.10 on 2020-06-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_remove_product_month_6'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='month_6',
            field=models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=9, verbose_name='Kredit 6 ay ucun ayliq odenis'),
            preserve_default=False,
        ),
    ]
