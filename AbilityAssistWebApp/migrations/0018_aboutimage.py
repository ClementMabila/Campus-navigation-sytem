# Generated by Django 5.0.4 on 2024-05-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AbilityAssistWebApp', '0017_trip_cancelled'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
