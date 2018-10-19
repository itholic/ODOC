# very shortend getting started

튜토리얼 매우 요약

## virtualenv 생성 및 구동
```
python -m virtualenv myvenv
source myvenv/bin/activate
```

## django 설치 및 'test_project' 프로젝트 생성
```
pip install django
django-admin startproject test_project
```

## 'blog' app 생성 및 model, view, url 설정
```
python manage.py start appblog
```
```python
# blog/models.py

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=256)
    contents = models.TextField()
    reg_date = models.DateTimeField(default=timezone.now)
```
```python
# blog/views.py

from django.http import HttpResponse

def post_main(request):
    return HttpResponse("check it out")
```
```python
# blog/urls.py

from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_main)
]
```

## app 및 url 추가
```python
# temp_project/settings.py

...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]

...
```
```python
# temp_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
```

## db 정보 생성 및 추가 (migration)
```
python manage.py makemigrations
python manage.py migrate
```

## 서버 구동 및 확인
```
python manage.py runserver 0.0.0.0:8000
브라우저에서 localhost:8000 접속 후 화면 확인
```
