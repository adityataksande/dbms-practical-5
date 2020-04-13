# Generated by Django 3.0.5 on 2020-04-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.IntegerField(unique=True)),
                ('daa', models.IntegerField()),
                ('dbms', models.IntegerField()),
                ('sepm', models.IntegerField()),
                ('sp', models.IntegerField()),
                ('total', models.IntegerField()),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]