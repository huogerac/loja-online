# Generated by Django 5.0.2 on 2024-03-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0002_alter_categoria_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.CharField(max_length=32),
        ),
    ]
