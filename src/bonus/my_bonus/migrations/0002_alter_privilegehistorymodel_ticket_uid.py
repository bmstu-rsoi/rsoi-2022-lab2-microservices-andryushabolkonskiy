from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('my_bonus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privilegehistorymodel',
            name='ticket_uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
