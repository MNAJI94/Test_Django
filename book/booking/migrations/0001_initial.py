# Generated by Django 3.1.4 on 2021-02-01 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artwork', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="date d'envoie")),
                ('contacted', models.BooleanField(default=False, verbose_name='demande traitée ?')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artwork.artwork')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.contact')),
            ],
            options={
                'verbose_name': 'réservation',
            },
        ),
    ]
