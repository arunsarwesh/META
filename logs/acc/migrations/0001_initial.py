# Generated by Django 5.0.7 on 2024-07-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=100)),
                ('Fname', models.CharField(max_length=50)),
            ],
        ),
    ]
