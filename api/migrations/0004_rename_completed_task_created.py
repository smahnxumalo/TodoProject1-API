# Generated by Django 4.1.5 on 2023-01-05 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_task_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='created',
        ),
    ]