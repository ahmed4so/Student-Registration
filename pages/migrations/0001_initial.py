# Generated by Django 5.0.1 on 2024-01-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('Date', models.DateField()),
                ('Faculty', models.CharField(choices=[('COMPUTING', 'COMPUTING'), ('Medcine', 'Medcine'), ('Health science', 'Health science'), ('Engineering', 'Engineering'), ('Account', 'Account')], max_length=100)),
                ('Phone', models.CharField(blank=True, max_length=20, null=True)),
                ('ADDRESS', models.CharField(max_length=200)),
                ('nex', models.CharField(max_length=150)),
            ],
        ),
    ]
