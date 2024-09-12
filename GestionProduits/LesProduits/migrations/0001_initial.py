# Generated by Django 5.1.1 on 2024-09-12 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('price_ht', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Prix unitaire HT')),
                ('price_ttc', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Prix unitaire TTC')),
                ('status', models.SmallIntegerField(choices=[(0, 'Offline'), (1, 'Online'), (2, 'Out of stock')], default=0)),
                ('date_creation', models.DateTimeField(blank=True, verbose_name='Date crÃ©ation')),
            ],
            options={
                'verbose_name': 'Produit',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Attribut',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LesProduits.productattribute', verbose_name='UnitÃ©')),
            ],
            options={
                'verbose_name': 'Valeur attribut',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('attributes', models.ManyToManyField(blank=True, null=True, related_name='product_item', to='LesProduits.productattributevalue')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LesProduits.product')),
            ],
            options={
                'verbose_name': 'DÃ©clinaison Produit',
            },
        ),
    ]
