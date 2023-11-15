# Generated by Django 4.2.7 on 2023-11-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_imagesss_image_imagesss_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='Const_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Imagesss',
        ),
        migrations.AlterField(
            model_name='const_projects',
            name='images',
            field=models.ManyToManyField(to='projects.images'),
        ),
    ]