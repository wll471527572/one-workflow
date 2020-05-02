# Generated by Django 3.0.2 on 2020-05-02 04:12

from django.db import migrations, models
import tools.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='./tmp', verbose_name='上传文件')),
            ],
            options={
                'verbose_name': '文件上传',
                'verbose_name_plural': '文件上传',
            },
        ),
        migrations.CreateModel(
            name='RequestEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('url', models.CharField(db_index=True, max_length=255, verbose_name='请求URI')),
                ('method', models.CharField(db_index=True, max_length=20, verbose_name='请求方法')),
                ('query_string', models.TextField(verbose_name='请求内容')),
                ('user', models.CharField(max_length=255, null=True, verbose_name='用户')),
                ('remote_ip', models.CharField(db_index=True, max_length=50, null=True, verbose_name='请求IP')),
            ],
            options={
                'verbose_name': '请求事件',
                'verbose_name_plural': '请求事件',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='SimpleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('username', models.CharField(max_length=20, verbose_name='上传用户')),
                ('file', models.FileField(blank=True, upload_to=tools.storage.PathAndRename('./'), verbose_name='上传文件')),
                ('archive', models.CharField(blank=True, default='其他', max_length=201, null=True, verbose_name='文件归档')),
                ('filename', models.CharField(blank=True, max_length=201, null=True, verbose_name='文件名')),
                ('filepath', models.CharField(blank=True, max_length=201, null=True, verbose_name='文件路径')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='文件类型')),
                ('size', models.CharField(blank=True, max_length=20, null=True, verbose_name='文件大小')),
            ],
            options={
                'verbose_name': '文件上传',
                'verbose_name_plural': '文件上传',
            },
        ),
    ]
