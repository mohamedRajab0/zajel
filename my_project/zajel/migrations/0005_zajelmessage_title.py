# Generated by Django 5.0.6 on 2024-07-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zajel', '0004_alter_zajelmessage_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='zajelmessage',
            name='title',
            field=models.CharField(default='message', max_length=50),
        ),
    ]
