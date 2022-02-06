# Generated by Django 4.0.1 on 2022-02-04 09:08

from django.db import migrations, models
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_usname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usname', models.CharField(max_length=200, unique=True, verbose_name='Username')),
                ('user_fname', models.CharField(max_length=200, verbose_name='First Name')),
                ('user_lname', models.CharField(max_length=200, verbose_name='Last Name')),
                ('user_email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('user_college', models.CharField(choices=[('CAUP', 'CAUP'), ('Education', 'Education'), ('CET', 'CET'), ('CHASS', 'CHASS'), ('Medicine', 'Medicine'), ('Nursing', 'Nursing'), ('PT', 'PT'), ('CS', 'CS'), ('Law', 'Law')], default='CET', max_length=10, verbose_name='College')),
                ('user_year', models.IntegerField(verbose_name='Year')),
                ('user_course', models.CharField(max_length=200, verbose_name='Course')),
                ('user_address', models.CharField(max_length=200, verbose_name='Address')),
                ('user_gender', models.CharField(max_length=100, verbose_name='Gender')),
                ('user_contactnumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Contact Number')),
                ('user_birthdate', models.DateField(verbose_name='Birthdate')),
                ('user_image', models.ImageField(default='profile_pic/default_profile_image.jpg', upload_to=users.models.image_path, verbose_name='Profile Picture')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]