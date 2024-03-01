# Generated by Django 4.2.3 on 2024-03-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_alter_donormodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donormodel',
            name='blood_group',
            field=models.CharField(choices=[('1', 'a+'), ('2', 'a-'), ('3', 'b+'), ('4', 'b-'), ('5', 'ab+'), ('6', 'ab-'), ('7', 'o+'), ('8', 'o-')], max_length=10),
        ),
    ]