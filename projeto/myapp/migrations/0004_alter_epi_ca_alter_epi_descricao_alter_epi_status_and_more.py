# Generated by Django 5.1 on 2024-09-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_epi_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epi',
            name='ca',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='epi',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='epi',
            name='status',
            field=models.CharField(choices=[('disponível', 'Disponível'), ('emprestado', 'Emprestado')], default='disponível', max_length=20),
        ),
        migrations.AlterField(
            model_name='epi',
            name='tipo',
            field=models.CharField(max_length=50),
        ),
    ]
