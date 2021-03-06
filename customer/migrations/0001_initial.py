# Generated by Django 2.1.5 on 2019-02-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField()),
                ('staff_msa_id', models.CharField(max_length=250)),
                ('store_name', models.CharField(max_length=250)),
                ('customer_name', models.CharField(max_length=250)),
                ('customer_phone', models.BigIntegerField()),
                ('device_make_model', models.CharField(max_length=250)),
                ('imei_number', models.BigIntegerField()),
                ('package_name', models.CharField(max_length=250)),
                ('pf_package_variant', models.CharField(max_length=250, null=True)),
                ('pf_120_detail', models.CharField(max_length=250, null=True)),
                ('pf_80_detail', models.CharField(max_length=250, null=True)),
                ('dpb_package_variant', models.CharField(max_length=250, null=True)),
                ('dpb_190_detail', models.CharField(max_length=250, null=True)),
                ('dpb_160_detail', models.CharField(max_length=250, null=True)),
                ('dpb_120_detail', models.CharField(max_length=250, null=True)),
                ('dpb_80_detail', models.CharField(max_length=250, null=True)),
                ('agreement_1', models.CharField(max_length=250)),
                ('agreement_2', models.CharField(max_length=250)),
            ],
        ),
    ]
