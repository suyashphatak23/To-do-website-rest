# Generated by Django 4.1.4 on 2022-12-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.CharField(max_length=100),
        ),
    ]