# Generated by Django 2.1.1 on 2018-10-11 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('job_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('job_url', models.CharField(max_length=100)),
                ('com_name', models.CharField(max_length=50)),
                ('com_url', models.CharField(max_length=100)),
                ('com_id', models.CharField(max_length=100)),
                ('com_address', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('date_stamp', models.FloatField()),
                ('salary_min', models.FloatField()),
                ('salary_max', models.FloatField()),
                ('apply', models.ManyToManyField(to='user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='toudi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_time', models.DateTimeField(auto_now_add=True)),
                ('kw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('yh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
    ]