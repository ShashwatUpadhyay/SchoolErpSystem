# Generated by Django 3.0.5 on 2024-11-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten'), ('eleven', 'eleven'), ('twelve', 'twelve')], default='one', max_length=10),
        ),
    ]