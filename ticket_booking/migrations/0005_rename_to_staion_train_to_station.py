# Generated by Django 4.1.7 on 2023-03-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0004_alter_train_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='to_staion',
            new_name='to_station',
        ),
    ]
