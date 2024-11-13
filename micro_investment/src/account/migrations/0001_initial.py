# Generated by Django 4.2.6 on 2023-10-30 11:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='balance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], default='single', max_length=50, verbose_name='Martial Status')),
                ('employment_status', models.CharField(choices=[('working', 'Working'), ('unemployed', 'Unemployed')], default='working', max_length=50, verbose_name='Employment Status')),
                ('housing_status', models.CharField(choices=[('renting', 'Renting'), ('own home', 'Own Home')], default='own home', max_length=50, verbose_name='Housing Status')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Phone Number')),
                ('credit_cart_number', models.CharField(max_length=100, verbose_name='Credit Cart Number')),
                ('debt_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Debt Amount')),
                ('monthly_income', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Monthly Income')),
                ('profile_picture', models.ImageField(upload_to='investor/profile_pictures/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])], verbose_name='Profile Picture')),
                ('about', models.TextField(blank=True, null=True, verbose_name='about')),
                ('business_activities', models.TextField(blank=True, null=True, verbose_name='Business Activities')),
                ('references', models.ManyToManyField(blank=True, related_name='investors', to=settings.AUTH_USER_MODEL, verbose_name='References')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='investor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_place', models.CharField(max_length=100, verbose_name='Experience Place')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
                ('start_year', models.PositiveIntegerField(default=2023, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2023)], verbose_name='start_year')),
                ('end_year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2023)], verbose_name='end_year')),
                ('is_continue', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_place', models.CharField(max_length=100, verbose_name='Education Place')),
                ('education_branch', models.CharField(max_length=100, verbose_name='Education Branch')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('start_year', models.PositiveIntegerField(default=2023, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2023)], verbose_name='Start Year')),
                ('end_year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2023)], verbose_name='End Year')),
                ('is_continue', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]