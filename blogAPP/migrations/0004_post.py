# Generated by Django 4.0.4 on 2022-05-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPP', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
