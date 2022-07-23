# Generated by Django 4.0.6 on 2022-07-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0002_alter_bid_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder_name',
            field=models.CharField(default='string', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='vote',
            field=models.CharField(choices=[('1', 'Shreya Ananad'), ('2', 'Shubham Upadhyay'), ('3', 'Raashid Altaf')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]