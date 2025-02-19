import json
import datetime

from django.shortcuts import render
from django.views import View
from library.models import Books, BorrowRecord
from users.models import Users
from django.core.paginator import Paginator
from django.http import JsonResponse
from utils.response import json_success_resp, json_fail_resp
from utils.resp_code import PARAMS_ERR


# Create your views here.
class LibraryView(View):

    def get(self, request):
        page = request.GET.get('page', 0)
        per_page = request.GET.get('per_page', 10)
        name = request.GET.get('name', None)
        author = request.GET.get('author', None)
        start_time = request.GET.get('start_time', None)
        end_time = request.GET.get('end_time', None)

        books = Books.objects
        if name:
            books = books.filter(name__icontains=name)
        if author:
            books = books.filter(author__icontains=author)
        if start_time:
            books = books.filter(start_time__gte=start_time)
        if end_time:
            books = books.filter(end_time__lte=start_time)

        books = books.values('id', 'name', 'author')
        paginator = Paginator(books, per_page)
        page_obj = paginator.get_page(page)

        data = {
            'total': paginator.count,
            'list': list(page_obj)
        }

        return json_success_resp(data)

    def post(self, request):
        print("111111111111111111111")
        request_data = json.loads(request.body.decode('utf-8'))
        name = request_data.get('name', None)
        author = request_data.get('author', None)
        if not all([name, author]):
            return json_fail_resp(PARAMS_ERR, '参数不足')

        book = Books(name=name, author=author)
        book.save()
        return json_success_resp({})

    def patch(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        id = request_data.get('id', None)
        name = request_data.get('name', None)
        author = request_data.get('author', None)
        if not all([id, name, author]):
            return json_fail_resp(PARAMS_ERR, '参数不足')

        Books.objects.filter(id=id).update(name=name, author=author)
        return json_success_resp({})

    def delete(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        id = request_data.get('id', None)
        if not id:
            return json_fail_resp(PARAMS_ERR, '参数不足')

        Books.objects.filter(id=id).delete()
        return json_success_resp({})


class BorrowBooksView(View):

    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        # 这里根据需求可以修改成接受列表，即可以同时借多本
        book_id = request_data.get('id', None)
        # request.user  本来应该在这里面去取用户，因为题目没要求登录方面的开发，为了方便直接从参数获取
        user_id = request_data.get('user_id', None)
        if not all([book_id, user_id]):
            return json_fail_resp(PARAMS_ERR, '参数不足')

        book = Books.objects.filter(id=book_id).first()
        if not book:
            return json_fail_resp(PARAMS_ERR, '该书籍不存在')
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return json_fail_resp(PARAMS_ERR, '该用户不存在')

        if BorrowRecord.objects.filter(book=book, status=False).first():
            return json_fail_resp(10001, '当前该书籍已被借阅')

        record = BorrowRecord(borrow_user=user, book=book)
        record.save()
        return json_success_resp({})


class ReturnBooksView(View):

    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        # 这里根据需求可以修改成接受列表，即可以同时借多本
        book_id = request_data.get('id', None)
        # request.user  本来应该在这里面去取用户，因为题目没要求登录方面的开发，为了方便直接从参数获取
        user_id = request_data.get('user_id', None)
        if not all([book_id, user_id]):
            return json_fail_resp(PARAMS_ERR, '参数不足')

        book = Books.objects.filter(id=book_id).first()
        if not book:
            return json_fail_resp(PARAMS_ERR, '该书籍不存在')
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return json_fail_resp(PARAMS_ERR, '该用户不存在')

        record = BorrowRecord.objects.filter(borrow_user=user, book=book, status=False).first()

        if not record:
            return json_fail_resp(10002, '当前用户未借阅该书籍')

        record.status = True
        record.return_time = datetime.datetime.now()
        record.save()
        return json_success_resp({})

