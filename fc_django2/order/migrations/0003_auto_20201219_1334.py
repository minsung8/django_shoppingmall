# Generated by Django 3.1.4 on 2020-12-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201219_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('대기중', '대기중'), ('결제대기', '결제대기'), ('결제완료', '결제완료'), ('환불', '환불')], default='대기중', max_length=32, verbose_name='상태'),
        ),
    ]