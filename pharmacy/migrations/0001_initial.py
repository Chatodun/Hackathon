# Generated by Django 2.2.6 on 2019-10-24 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Введите адрес', max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(help_text='Введите телефон', max_length=13, verbose_name='Телефон')),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название препарата', max_length=150, verbose_name='Название')),
                ('image', models.ImageField(upload_to='')),
                ('manual', models.TextField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('purpose', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название организации', max_length=150, verbose_name='Название организации')),
                ('delivery', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicamentInPharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField()),
                ('count', models.PositiveSmallIntegerField()),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Medicament')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Organization', verbose_name='Организация'),
        ),
    ]
