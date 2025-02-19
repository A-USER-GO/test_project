from django.db import models
from users.models import Users

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = '图书表'
        verbose_name = '图书表'


class BorrowRecord(models.Model):
    status = models.BooleanField(default=False, verbose_name='是否归还 True归还 False 未归还')
    borrow_user = models.ForeignKey(Users, verbose_name='用户', on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Books, verbose_name='书籍', on_delete=models.DO_NOTHING)
    borrow_time = models.DateTimeField(auto_now_add=True, verbose_name='借阅时间')
    return_time = models.DateTimeField(null=True, blank=True, verbose_name='归还时间')

    class Meta:
        verbose_name_plural = '图书借阅记录表'
        verbose_name = '图书借阅记录表'