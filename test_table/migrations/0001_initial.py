# Generated by Django 3.2.7 on 2021-09-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=52)),
                ('quantity', models.IntegerField()),
                ('distance', models.IntegerField()),
            ],
        ),
    ]