# Generated by Django 4.1.2 on 2022-10-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_noticias_contenido_alter_noticias_sub_titulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='fecha',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
