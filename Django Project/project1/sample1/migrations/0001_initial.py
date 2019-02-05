# Generated by Django 2.1.5 on 2019-02-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(null=True)),
                ('species', models.CharField(max_length=200)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField()),
                ('submission_date', models.DateTimeField()),
                ('submitter', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccination',
            field=models.ManyToManyField(blank=True, to='sample1.Vaccine'),
        ),
    ]
