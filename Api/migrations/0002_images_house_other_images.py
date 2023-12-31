# Generated by Django 4.2.2 on 2023-06-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='other_images')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='other_images',
            field=models.ManyToManyField(blank=True, to='Api.images'),
        ),
    ]
