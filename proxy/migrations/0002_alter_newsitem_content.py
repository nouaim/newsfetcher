# Generated by Django 5.0.1 on 2024-01-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
