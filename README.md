# test_project

# 设计一个图书馆管理系统，维护图书相关的属性
# 提供图书的查询、录入、修改和销毁的 API
  # 这部分可以用django-rest-framework框架实现更快，当前要求用django就没有去用别的框架
  录入：127.0.0.1:8000/library/books  请求方式：POST
  修改：127.0.0.1:8000/library/books  请求方式：PATCH
  销毁：127.0.0.1:8000/library/books  请求方式：DELETE
  查询列表：127.0.0.1:8000/library/books  请求方式：GET
# 提供借书、还书的 API
  借书：127.0.0.1:8000/library/borrow_book  请求方式：POST
  还书：127.0.0.1:8000/library/return_book  请求方式：POST
# 图书借阅期限为 30 天，每天 08:00 发通知将在 7 天内到期的图书借阅者，提醒还书
  使用win10启动时要注意，参考：https://blog.csdn.net/PY0312/article/details/105538699
# 实现一个中间件，记录每个 API 请求的参数和耗时
  暂时输出到终端，正式环境应该写入日志
  
# 安装依赖
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  -r .\requirements
# win10启动
  记得修改mysql、redis配置
  python manage runserver
  # -P参数win10必须加上
  celery -A test_project.celery worker --loglevel=info -P eventlet
  celery -A test_project.celery beat --loglevel=info