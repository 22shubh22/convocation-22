# Generated by Django 4.0.6 on 2022-07-18 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bid_amount', models.IntegerField(blank=True, null=True)),
                ('vote', models.CharField(blank=True, choices=[('1', 'shreya ananad'), ('2', 'shubham upadhyay'), ('3', 'rashid altaf')], max_length=2, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
