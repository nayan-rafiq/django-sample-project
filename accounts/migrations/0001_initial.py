# Generated by Django 4.2.7 on 2023-11-12 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')])),
                ('highest_education', models.IntegerField(choices=[(1, 'SSC'), (2, 'HSC'), (3, 'Honours'), (4, 'Masters'), (5, 'Phd')])),
                ('job_search_status', models.IntegerField(choices=[(1, 'Closed'), (2, 'Open to offers'), (3, 'Actively seeking')])),
                ('years_of_experiences', models.PositiveSmallIntegerField()),
                ('monthly_expected_salary', models.PositiveIntegerField()),
                ('resume', models.FileField(upload_to='resumes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
