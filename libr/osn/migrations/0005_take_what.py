# Generated by Django 5.0.7 on 2024-07-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osn', '0004_take'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='what',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
