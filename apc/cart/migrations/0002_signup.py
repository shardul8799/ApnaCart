# Generated by Django 2.2.5 on 2019-10-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ussername', models.CharField(max_length=50)),
                ('password', models.CharField(default='', max_length=70)),
                ('phone', models.IntegerField(default='', max_length=70)),
            ],
        ),
    ]
