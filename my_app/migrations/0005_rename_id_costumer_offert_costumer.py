# Generated by Django 4.1.1 on 2022-09-18 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_offert_value_type_alter_offert_from_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offert',
            old_name='id_costumer',
            new_name='costumer',
        ),
    ]
