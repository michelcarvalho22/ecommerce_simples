# Generated by Django 2.0.1 on 2018-02-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20180210_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], default='deposit', max_length=20, verbose_name='Opção de Pagamento'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete='Pedido', to='checkout.Order', verbose_name='items'),
        ),
    ]