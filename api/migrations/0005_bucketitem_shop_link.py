# Generated by Django 3.2.6 on 2021-08-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_bucketitem_pict'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketitem',
            name='shop_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
