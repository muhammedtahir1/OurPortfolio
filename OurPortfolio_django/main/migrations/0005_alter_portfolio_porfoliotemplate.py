# Generated by Django 4.2 on 2023-06-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_portfolio_porfoliotemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='porfolioTemplate',
            field=models.CharField(choices=[('BLUE', 'Blue Theme'), ('CREAM', 'Elegent Cream'), ('DEFAULT', 'Default Theme'), ('DARK', 'Dark Woods')], default='DEFAULT', max_length=10),
        ),
    ]
