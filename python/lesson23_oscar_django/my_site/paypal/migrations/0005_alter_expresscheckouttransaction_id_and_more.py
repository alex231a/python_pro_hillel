# Generated by Django 4.2.20 on 2025-04-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal', '0004_increase_max_char_length_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expresscheckouttransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='expresstransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payflowtransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
