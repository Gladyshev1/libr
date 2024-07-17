# Generated by Django 5.0.7 on 2024-07-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
