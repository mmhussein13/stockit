# Generated by Django 3.0.7 on 2023-02-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20230209_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='part_number',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
