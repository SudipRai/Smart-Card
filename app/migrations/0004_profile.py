# Generated by Django 3.0.8 on 2020-07-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='img.jpg', upload_to='')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('google', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('youtube', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
