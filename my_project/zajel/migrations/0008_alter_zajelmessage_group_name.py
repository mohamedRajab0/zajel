# Generated by Django 5.0.6 on 2024-07-04 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zajel', '0007_rename_date_zajelmessage_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zajelmessage',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='zajel.zajelgroup'),
        ),
    ]
