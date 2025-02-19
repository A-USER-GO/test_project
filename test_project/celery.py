import os
from celery import Celery
from celery.schedules import crontab

# 设置 Django 的默认 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

app = Celery('test_project')

# 读取 Django 的配置
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Asia/Shanghai'

# 自动发现任务
app.autodiscover_tasks(['library'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
