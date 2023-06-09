# Generated by Django 4.1 on 2023-04-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photo')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
                'db_table': 'web_about',
                'ordering': ('id',),
            },
        ),
    ]
