# Generated by Django 5.0.3 on 2024-06-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]