# Generated by Django 4.1.2 on 2022-10-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_juego_reseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='contenido',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='sub_titulo',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
