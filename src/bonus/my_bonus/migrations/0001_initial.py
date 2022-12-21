from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivilegeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80, unique=True)),
                ('status', models.CharField(choices=[('BRONZE', 'Bronze'), ('SILVER', 'Silver'), ('GOLD', 'Gold')], default='BRONZE', max_length=80)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivilegeHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('datetime', models.DateTimeField()),
                ('balance_diff', models.IntegerField()),
                ('operation_type', models.CharField(choices=[('FILL_IN_BALANCE', 'fill_in_balance'), ('DEBIT_THE_ACCOUNT', 'debit_the_account')], max_length=20)),
                ('privilege_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_bonus.privilegemodel')),
            ],
        ),
    ]
