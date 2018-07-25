# Generated by Django 2.0.2 on 2018-07-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('tuning_time', models.FloatField(default=0.0)),
                ('throughput', models.FloatField(default=0.0)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('shared_buffers', models.IntegerField(choices=[('1', '3'), ('2', '9'), ('3', '27')])),
                ('effective_io_concurrency', models.IntegerField(choices=[('1', '1'), ('2', '2')])),
            ],
        ),
        migrations.CreateModel(
            name='KnobCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('default', models.IntegerField()),
                ('setting', models.CharField(max_length=200))
            ],
        ),
    ]