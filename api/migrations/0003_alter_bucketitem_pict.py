# Generated by Django 3.2.6 on 2021-08-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bucket_bucketitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketitem',
            name='pict',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
