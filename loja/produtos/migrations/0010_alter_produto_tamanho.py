# Generated by Django 5.0.2 on 2024-04-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_alter_produto_tamanho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'), ('GG', 'Extra Grande'), ('ACS', 'Acessório'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44')], max_length=50),
        ),
    ]
