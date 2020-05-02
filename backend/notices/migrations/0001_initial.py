# Generated by Django 3.0.2 on 2020-05-02 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('type', models.CharField(choices=[('mail', 'mail'), ('telegram', 'telegram')], default=0, max_length=10, verbose_name='通知类型')),
                ('name', models.CharField(max_length=112, unique=True, verbose_name='名称')),
                ('host', models.CharField(max_length=112, verbose_name='主机')),
                ('user', models.CharField(max_length=112, verbose_name='账号')),
                ('password', models.CharField(max_length=112, verbose_name='密码')),
                ('to', models.CharField(max_length=112, verbose_name='接收者')),
            ],
            options={
                'verbose_name': '邮件机器人',
                'verbose_name_plural': '邮件机器人',
            },
        ),
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('type', models.CharField(choices=[('mail', 'mail'), ('telegram', 'telegram')], default=0, max_length=10, verbose_name='通知类型')),
                ('name', models.CharField(max_length=112, unique=True, verbose_name='名称')),
                ('uid', models.CharField(max_length=112, verbose_name='账号id')),
                ('token', models.CharField(max_length=112, verbose_name='token')),
                ('chat_id', models.CharField(max_length=112, verbose_name='chat_id')),
            ],
            options={
                'verbose_name': 'tg机器人',
                'verbose_name_plural': 'tg机器人',
            },
        ),
    ]
