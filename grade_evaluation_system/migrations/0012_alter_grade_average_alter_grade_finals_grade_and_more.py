# Generated by Django 5.1.3 on 2024-11-17 07:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_evaluation_system', '0011_alter_grade_average_alter_grade_finals_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='average',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='finals_grade',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='mid_terms_grade',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
