# Generated by Django 2.2.8 on 2019-12-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catone', '0003_catone_papers_relative_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_portal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('options', models.CharField(max_length=10)),
                ('correct_option', models.CharField(max_length=10)),
                ('quiz', models.CharField(max_length=20)),
                ('points', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='catone_papers',
        ),
    ]
