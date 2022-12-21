from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FlightModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('from_airport_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_airport_id', to='my_flight.airportmodel')),
                ('to_airport_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_airport_id', to='my_flight.airportmodel')),
            ],
        ),
    ]
