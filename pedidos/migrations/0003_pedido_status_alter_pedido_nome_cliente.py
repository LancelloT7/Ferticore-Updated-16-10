# Generated by Django 5.1.1 on 2024-10-20 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('pedidos', '0002_pedido_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluído', 'Concluído'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nome_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente'),
        ),
    ]
