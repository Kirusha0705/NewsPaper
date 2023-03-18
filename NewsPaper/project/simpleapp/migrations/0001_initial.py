# Generated by Django 4.1.7 on 2023-03-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('name_author', models.TextField()),
            ],
        ),
    ]
