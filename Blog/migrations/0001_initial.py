# Generated by Django 4.1 on 2022-08-25 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog')),
                ('content', models.CharField(max_length=1000)),
                ('puplishdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
