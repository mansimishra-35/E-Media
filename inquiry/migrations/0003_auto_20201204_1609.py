# Generated by Django 2.2.5 on 2020-12-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_auto_20201204_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]