# Generated by Django 4.2.7 on 2023-11-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_const_projects_images_alter_photos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(null=True, upload_to='Const_photos'),
        ),
    ]
