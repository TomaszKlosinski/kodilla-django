# Generated by Django 4.2 on 2023-05-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='operation',
            field=models.CharField(choices=[('add', 'add'), ('sub', 'sub'), ('mul', 'mul'), ('div', 'div')], max_length=5),
        ),
    ]
