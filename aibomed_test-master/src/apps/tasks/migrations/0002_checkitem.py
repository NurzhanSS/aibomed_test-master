# Generated by Django 3.2.8 on 2021-10-26 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126, verbose_name='Name')),
                ('is_done', models.BooleanField(default=False, verbose_name='Done')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_items', to='tasks.task', verbose_name='Task')),
            ],
            options={
                'verbose_name': 'Checklist Item',
                'verbose_name_plural': 'Checklist Items',
            },
        ),
    ]
