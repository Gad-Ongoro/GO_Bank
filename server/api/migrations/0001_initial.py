# Generated by Django 5.1.1 on 2024-10-06 11:22

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('account_number', models.IntegerField()),
                ('relation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
                ('open_days', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('permission', models.CharField(choices=[('can_only_read_transactions', 'Read Only'), ('can_crud_transactions', 'Full CRUD'), ('can_only_create_transactions', 'Create Only')], max_length=50)),
            ],
            options={
                'permissions': [('can_only_read_transactions', 'Can only view transactions'), ('can_crud_transactions', 'Can CRUD transactions'), ('can_only_create_transactions', 'Can only create transactions')],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.IntegerField(choices=[(10, 'Admin'), (100, 'Employee'), (1000, 'User')], default=1000)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('primary_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.branch')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_type', models.CharField(max_length=50)),
                ('account_number', models.IntegerField(unique=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('loan_limit', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('card_number', models.IntegerField(unique=True)),
                ('CVV', models.IntegerField()),
                ('date_issued', models.CharField(default='10/24', max_length=50)),
                ('expiration_date', models.CharField(default='10/28', max_length=50)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bank_account')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration', models.PositiveIntegerField(help_text='Loan period in months')),
                ('collateral', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('due_date', models.DateField()),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bank_account')),
            ],
        ),
        migrations.CreateModel(
            name='Loan_Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_paid', models.IntegerField()),
                ('last_pay_amount', models.IntegerField()),
                ('upcoming_pay_amount', models.IntegerField()),
                ('last_pay_date', models.DateTimeField(auto_now=True)),
                ('upcoming_pay_date', models.CharField(max_length=50)),
                ('balance', models.IntegerField()),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bank_account')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.loan')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('backup_mail', models.EmailField(max_length=254, unique=True)),
                ('ID_type', models.CharField(max_length=100)),
                ('ID_number', models.IntegerField()),
                ('country_of_residence', models.CharField(max_length=100)),
                ('profile_photo', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('result_description', models.TextField(blank=True, null=True)),
                ('receipt_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('credit', 'Deposit'), ('debit', 'Withdrawal')], max_length=10)),
                ('bank_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.bank_account')),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.beneficiary')),
                ('investment_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.investmentaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInvestmentAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('investment_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.investmentaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'investment_account')},
            },
        ),
        migrations.AddField(
            model_name='investmentaccount',
            name='users',
            field=models.ManyToManyField(through='api.UserInvestmentAccount', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='investment_accounts',
            field=models.ManyToManyField(blank=True, through='api.UserInvestmentAccount', to='api.investmentaccount'),
        ),
    ]
