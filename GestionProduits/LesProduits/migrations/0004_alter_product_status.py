# Generated by Django 5.1.1 on 2024-09-11 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LesProduits', '0003_alter_product_code_alter_productitem_code_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LesProduits.status'),
        ),
    ]
