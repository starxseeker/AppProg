# Generated by Django 3.2.9 on 2021-12-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20211202_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='total_borrow_count',
            field=models.IntegerField(default=0),
        ),
    ]
