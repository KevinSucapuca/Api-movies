# Generated by Django 4.1.7 on 2023-03-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
