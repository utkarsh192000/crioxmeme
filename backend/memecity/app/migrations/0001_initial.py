# Generated by Django 3.0.8 on 2021-02-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=1000000)),
            ],
        ),
    ]
