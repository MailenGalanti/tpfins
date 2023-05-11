# Generated by Django 4.2 on 2023-05-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_analysis', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('industry', models.CharField(max_length=256)),
                ('credit_rating_borrower', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
