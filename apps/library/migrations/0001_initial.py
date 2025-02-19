# Generated by Django 3.2 on 2025-02-19 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '图书表',
                'verbose_name_plural': '图书表',
            },
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='是否归还 True归还 False 未归还')),
                ('borrow_time', models.DateTimeField(auto_now_add=True, verbose_name='借阅时间')),
                ('return_time', models.DateTimeField(verbose_name='归还时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.books', verbose_name='书籍')),
            ],
            options={
                'verbose_name': '图书借阅记录表',
                'verbose_name_plural': '图书借阅记录表',
            },
        ),
    ]
