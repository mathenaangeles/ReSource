# Generated by Django 2.2.1 on 2020-01-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200124_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_pictures'),
        ),
    ]