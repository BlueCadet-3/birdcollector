# Generated by Django 3.1.2 on 2020-12-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('continent', models.CharField(choices=[('AF', 'Africa'), ('ANT', 'Antarctica'), ('AS', 'Asia'), ('AUS', 'Australia'), ('EU', 'Europe'), ('NA', 'North America'), ('SA', 'South America')], default='AF', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
        migrations.AddField(
            model_name='bird',
            name='locations',
            field=models.ManyToManyField(to='main_app.Location'),
        ),
    ]
