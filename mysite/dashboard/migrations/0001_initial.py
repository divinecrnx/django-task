# Generated by Django 3.1.5 on 2021-01-08 06:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_num', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('vehicle_model_year', models.CharField(max_length=6)),
                ('vehicle_model', models.CharField(max_length=60)),
                ('vehicle_no', models.CharField(max_length=20)),
                ('accident_dt', models.DateTimeField()),
                ('location', models.CharField(max_length=80)),
                ('loss_type', models.CharField(choices=[('OD', 'Own Damage'), ('KFK', 'Knock for Knock'), ('WD', 'Windscreen Damage'), ('T', 'Theft')], default='OD', max_length=3)),
                ('loss_desc', models.TextField()),
                ('pr_lodged_inq', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3)),
                ('inq_injury', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('photo', models.ImageField(upload_to='images/')),
                ('insurance_cover_note_pdf', models.FileField(upload_to='')),
            ],
        ),
    ]