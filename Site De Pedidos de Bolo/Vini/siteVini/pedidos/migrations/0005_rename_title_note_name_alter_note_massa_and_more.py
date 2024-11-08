# Generated by Django 5.1.1 on 2024-10-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_note_massa_note_recheio_note_topo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='note',
            name='massa',
            field=models.CharField(choices=[('n/a', 'N/A'), ('chocolate', 'Chocolate'), ('fubá', 'Fuba'), ('cenoura', 'Cenoura')], default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='note',
            name='recheio',
            field=models.CharField(choices=[('n/a', 'N/A'), ('chocolate', 'Chocolate'), ('morango', 'Morango'), ('caramelo', 'Caramelo')], default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='note',
            name='size',
            field=models.CharField(choices=[('n/a', 'N/A'), ('pequeno', 'Pequeno'), ('medio', 'medio'), ('grande', 'grande')], default='N/A', max_length=20),
        ),
    ]
