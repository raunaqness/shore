# Generated by Django 3.2.9 on 2021-11-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_auto_20211105_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productalert',
            name='website',
            field=models.CharField(choices=[('EBAY', 'EBay'), ('AMAZON', 'Amazon')], default=('EBAY', 'EBay'), max_length=20),
        ),
    ]