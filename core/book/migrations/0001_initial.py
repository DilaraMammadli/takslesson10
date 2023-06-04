# Generated by Django 4.2.1 on 2023-06-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]