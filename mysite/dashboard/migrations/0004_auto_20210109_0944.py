# Generated by Django 3.1.5 on 2021-01-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_claim_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Accepted', 'Accepted')], default='In Progress', max_length=11),
        ),
    ]