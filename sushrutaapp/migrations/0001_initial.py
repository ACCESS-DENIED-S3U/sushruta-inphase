# Generated by Django 3.2.6 on 2021-08-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_name', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=0)),
                ('address', models.CharField(default='', max_length=50)),
                ('designation', models.CharField(default='', max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(default='', max_length=50)),
                ('license_no', models.CharField(blank=True, max_length=300, unique=True)),
                ('speciality', models.CharField(default='', max_length=100)),
                ('tags', models.CharField(default='[]', max_length=500)),
                ('rating', models.IntegerField(default=0, null=True)),
                ('isVerified', models.BooleanField(blank=True, default=True, null=True)),
                ('Users_D', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sushrutaapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Users_P', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sushrutaapp.users')),
            ],
        ),
    ]
