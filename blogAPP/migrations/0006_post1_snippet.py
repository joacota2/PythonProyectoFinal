# Generated by Django 4.0.4 on 2022-05-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPP', '0005_post1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post1',
            name='snippet',
            field=models.CharField(default='Resumen', max_length=255),
        ),
    ]
