# Generated by Django 3.0.5 on 2020-05-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yardimtalepler', '0004_auto_20200502_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='yardimlar',
            name='userid',
            field=models.TextField(null=True),
        ),
    ]
