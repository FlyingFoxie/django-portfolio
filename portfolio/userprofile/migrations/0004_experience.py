# Generated by Django 3.1 on 2020-11-25 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20201125_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('job_title', models.CharField(max_length=200, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('job_description', models.TextField(null=True)),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='userprofile.profile')),
            ],
        ),
    ]
