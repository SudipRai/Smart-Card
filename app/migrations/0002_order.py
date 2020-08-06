# Generated by Django 3.0.8 on 2020-07-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=100)),
                ('totalcost', models.IntegerField(max_length=100)),
                ('cardname', models.CharField(max_length=100)),
                ('cardnumber', models.CharField(max_length=100)),
                ('cvv', models.CharField(max_length=100)),
                ('expiration', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]