# Generated by Django 5.1.3 on 2025-02-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdbiorcyZestawu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
