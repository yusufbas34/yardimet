# Generated by Django 3.0.5 on 2020-05-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yardimtalepler', '0006_auto_20200504_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='yardimlar',
            name='u_email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
