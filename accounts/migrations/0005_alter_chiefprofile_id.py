# Generated by Django 4.1 on 2023-04-13 13:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_chiefprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eb900100-8a9b-469b-90d0-9be160b5cadf'), editable=False, primary_key=True, serialize=False),
        ),
    ]