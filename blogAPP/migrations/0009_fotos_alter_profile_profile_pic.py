# Generated by Django 4.0.4 on 2022-05-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPP', '0008_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='images/fotos/')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
