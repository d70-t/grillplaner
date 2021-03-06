# Generated by Django 2.0.5 on 2018-05-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('attends', models.BooleanField()),
                ('count', models.PositiveIntegerField()),
                ('brings', models.CharField(max_length=1000)),
            ],
        ),
    ]
