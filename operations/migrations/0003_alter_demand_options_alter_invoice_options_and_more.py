# Generated by Django 4.0.4 on 2022-05-27 08:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0003_alter_contractor_category_alter_contractor_name_and_more'),
        ('operations', '0002_demand_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Счет', 'verbose_name_plural': 'Счета'},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='state',
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_handed',
            field=models.BooleanField(default=False, verbose_name='Выставлен клиенту'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачен'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='demand',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contractors.contractorsobject', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='state',
            field=models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В работе'), ('ordered', 'Размещена у поставщика'), ('on_store', 'Получена от поставщика'), ('delivered', 'Доставлена клиенту'), ('paid', 'Оплачена'), ('done', 'Закрыта')], default='Новая', max_length=255, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='contractors.contractorsobject', verbose_name='Объект'),
        ),
    ]
