# Generated by Django 4.0.4 on 2022-05-26 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='address',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contractors.contractorcategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contractorcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='contractorcategory',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='contractorsobject',
            name='contractor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contractors.contractor', verbose_name='Контрагент'),
        ),
        migrations.AlterField(
            model_name='contractorsobject',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='contractorsobject',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Наименование'),
        ),
    ]
