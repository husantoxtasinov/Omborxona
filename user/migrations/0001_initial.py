# Generated by Django 4.1.2 on 2022-10-10 04:48

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
            name='Sotuvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('manzil', models.CharField(max_length=60)),
                ('tel', models.CharField(max_length=11)),
                ('vazifa', models.CharField(blank=True, max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]