# Generated by Django 5.0.2 on 2024-03-19 00:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Infantil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Infantil', models.CharField(max_length=128)),
                ('descricao', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=512)),
                ('valor', models.CharField(max_length=32)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(upload_to='img/')),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='CarrinhoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produtos',
            field=models.ManyToManyField(through='produtos.CarrinhoItem', to='produtos.produto'),
        ),
    ]
