# Generated by Django 4.1 on 2023-04-13 11:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_chiefprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bc5d7bd9-ac7d-4055-83f0-1d675d26ba00'), editable=False, primary_key=True, serialize=False),
        ),
    ]
