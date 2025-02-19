from celery import shared_task
from datetime import datetime, timedelta
from library.models import BorrowRecord


@shared_task
def daily_task():
    records = BorrowRecord.objects.filter(status=False, borrow_time__lte=datetime.now() - timedelta(days=23))
    for r in records:
        borrow_user = r.borrow_user
        print('根据得到的用户去短信通知或者站内短信通知')