# Generated by Django 4.1 on 2023-04-14 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_chiefprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7e595644-f8ef-437a-8672-dd7e1ab88c9d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
