# Generated by Django 3.0.5 on 2020-08-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0006_auto_20200804_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmodel',
            name='year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]