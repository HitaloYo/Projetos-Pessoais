# Generated by Django 5.1.1 on 2024-10-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_note_recheio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='recheio',
            field=models.CharField(choices=[('n/a', 'N/A'), ('chocolate', 'Chocolate'), ('morango', 'Morango'), ('caramelo', 'Caramelo')], default='N/A', max_length=20),
        ),
    ]
