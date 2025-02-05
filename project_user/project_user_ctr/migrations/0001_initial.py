# Generated by Django 4.1.13 on 2024-07-15 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('institution', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('reg_no', models.CharField(max_length=50, unique=True)),
                ('ac_year', models.CharField(max_length=4)),
                ('course_year', models.CharField(max_length=4)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'register',
            },
        ),
        migrations.CreateModel(
            name='HostelApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('number_of_sharing', models.IntegerField()),
                ('mother_name', models.CharField(default='N/A', max_length=20)),
                ('occupation', models.CharField(default='N/A', max_length=20)),
                ('landline_num', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact', models.CharField(default='0000000000', max_length=15)),
                ('father_email', models.EmailField(default='father@example.com', max_length=50)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project_user_ctr.register')),
            ],
        ),
    ]
