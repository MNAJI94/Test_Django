# Generated by Django 3.1.4 on 2021-02-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField(null=True, verbose_name='référence')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('available', models.BooleanField(default=True, verbose_name='disponible')),
                ('title', models.CharField(max_length=200, verbose_name='titre du disque ')),
                ('photo', models.FileField(upload_to='photo/', verbose_name='URL dl image')),
                ('author', models.ManyToManyField(blank=True, related_name='arrtwork', to='author.Author')),
            ],
            options={
                'verbose_name': 'artwork',
            },
        ),
    ]
