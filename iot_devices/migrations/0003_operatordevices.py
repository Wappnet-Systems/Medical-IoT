# Generated by Django 3.1.3 on 2021-04-06 08:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iot_devices', '0002_remove_iotdevice_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='operatorDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_devices.iotdevice')),
                ('operator_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'operator_device',
            },
        ),
    ]