"""seolyupjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# 아래와 같이 쓰면 안됨
# from seolyupjt import settings
# 왜냐하면
# from django.conf import global_settings 가 합쳐져야하므로
# 위 기본에다가 저 위에 settings 를 overwrite 하는거라서
from django.conf import settings  # 위 두가지 합쳐준거

urlpatterns = [
    path('admin/', admin.site.urls),  # URL Reverse 기능
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
]

settings.MEDIA_URL
settings.MEDIA_ROOT

# DEBUG 참일 때
if settings.DEBUG:
    # url 리스트를 urlpatterns에 추가함
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)