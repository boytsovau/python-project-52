# Generated by Django 5.0.1 on 2024-02-12 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mark', '0001_initial'),
        ('status', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mark.mark')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to='users.taskuser')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.taskuser')),
                ('labels', models.ManyToManyField(blank=True, null=True, through='task.Bond', to='mark.mark')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='status.status')),
            ],
        ),
        migrations.AddField(
            model_name='bond',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
    ]
