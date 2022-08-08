# Generated by Django 4.0.6 on 2022-07-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255)),
                ('contenido', models.CharField(blank=True, max_length=255)),
                ('imagen', models.ImageField(upload_to='')),
                ('create', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
