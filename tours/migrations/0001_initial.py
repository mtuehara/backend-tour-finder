# Generated by Django 3.0.3 on 2020-03-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('date', models.DateField(verbose_name='Data')),
                ('full', models.BooleanField(verbose_name='Lotado')),
                ('vacancy', models.PositiveIntegerField(verbose_name='Vagas')),
                ('sold', models.PositiveIntegerField(verbose_name='Vendidos')),
                ('tour_type', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
        ),
    ]
