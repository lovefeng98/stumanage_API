# Generated by Django 3.1.4 on 2020-12-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='realname',
            field=models.CharField(default='', max_length=20, verbose_name='真实姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=300, verbose_name='token'),
        ),
    ]