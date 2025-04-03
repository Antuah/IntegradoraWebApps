# Generated by Django 5.1.4 on 2025-04-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('token_recuperacion', models.CharField(blank=True, max_length=255, null=True)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('normal', 'Usuario Normal')], default='normal', max_length=10)),
            ],
        ),
    ]
