# Generated by Django 5.1.3 on 2024-11-17 07:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_evaluation_system', '0006_alter_grade_average_alter_grade_finals_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='average',
            field=models.DecimalField(decimal_places=4, max_digits=12, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
