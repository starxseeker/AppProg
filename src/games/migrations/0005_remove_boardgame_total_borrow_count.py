# Generated by Django 3.2.9 on 2021-11-25 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_boardgame_total_borrow_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardgame',
            name='total_borrow_count',
        ),
    ]
