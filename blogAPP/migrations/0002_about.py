# Generated by Django 4.0.4 on 2022-05-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]