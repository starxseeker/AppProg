# Generated by Django 3.2.9 on 2021-11-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_remove_boardgame_total_borrow_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='total_borrow_count',
            field=models.IntegerField(default=0),
        ),
    ]
