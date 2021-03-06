# Generated by Django 3.1.2 on 2020-10-04 18:02

from django.db import migrations, models
import django.db.models.deletion
import sales.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=15)),
                ('trim', models.CharField(max_length=30)),
                ('year', models.IntegerField(choices=[(1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008'), (2009, '2009'), (2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019')], default=sales.models.Vehicle.current_year)),
                ('fuel', models.CharField(choices=[('1', 'Petrol'), ('2', 'Diesel'), ('3', 'Hybrid'), ('4', 'Electric')], default='1', max_length=8)),
                ('body_type', models.CharField(choices=[('1', 'Coupe'), ('2', 'Hatchback'), ('3', 'Saloon'), ('4', ' Estate'), ('5', 'Van'), ('6', 'Convertible')], default='1', max_length=8)),
                ('car_state', models.CharField(choices=[('1', 'Trade-in'), ('2', 'Frontline')], default='1', max_length=8)),
                ('reserved', models.CharField(choices=[('1', 'Reserved'), ('2', 'For Sale'), ('3', 'Sold')], default='1', max_length=8)),
                ('mileage', models.IntegerField()),
                ('engine_size', models.IntegerField()),
                ('mot_till', models.DateField()),
                ('extras', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vehicle_images')),
                ('order', models.IntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.vehicle')),
            ],
        ),
    ]
