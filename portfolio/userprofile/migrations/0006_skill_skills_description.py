# Generated by Django 3.1 on 2020-12-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_experience_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skills_description',
            field=models.TextField(null=True),
        ),
    ]
