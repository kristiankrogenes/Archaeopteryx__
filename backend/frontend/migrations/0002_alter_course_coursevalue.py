# Generated by Django 3.2.4 on 2021-06-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coursevalue',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
