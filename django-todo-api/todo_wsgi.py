import os
import sys

# مسیر پروژه رو اضافه کن به sys.path
project_path = '/home/user/django-todo'
sys.path.append(project_path)

# مسیر تنظیمات اصلی پروژه‌ات
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()