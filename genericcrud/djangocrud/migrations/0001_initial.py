# Generated by Django 5.0.3 on 2024-03-19 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
