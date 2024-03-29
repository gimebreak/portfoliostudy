# Generated by Django 2.1.12 on 2019-10-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=50),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='在这里写作品简介', max_length=100),
        ),
    ]
