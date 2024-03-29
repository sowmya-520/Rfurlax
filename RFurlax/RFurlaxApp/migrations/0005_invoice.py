# Generated by Django 4.1.13 on 2024-02-10 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RFurlaxApp', '0004_delete_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ORDERED', 'Ordered'), ('CANCELLED', 'Cancelled'), ('DELIVERED', 'Delivered')], max_length=50)),
                ('tenure', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RFurlaxApp.customer')),
                ('products', models.ManyToManyField(to='RFurlaxApp.product')),
            ],
        ),
    ]
