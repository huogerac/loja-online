# Generated by Django 5.0.2 on 2024-03-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.DeleteModel(
            name='Masculino',
        ),
    ]