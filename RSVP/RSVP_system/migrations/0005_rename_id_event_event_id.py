# Generated by Django 4.1.5 on 2023-02-07 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP_system', '0004_alter_event_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='id',
            new_name='event_id',
        ),
    ]