# Generated by Django 3.0.6 on 2020-05-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=50)),
                ('stuemail', models.EmailField(max_length=50)),
                ('stupass', models.CharField(max_length=50)),
            ],
        ),
    ]
