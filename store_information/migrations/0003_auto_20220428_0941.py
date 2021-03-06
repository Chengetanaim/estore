# Generated by Django 3.2.5 on 2022-04-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_information', '0002_hotdeals_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='estore',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to='store_information.EStore'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
