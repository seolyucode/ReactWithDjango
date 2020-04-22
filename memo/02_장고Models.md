## 장고 모델 (ORM)

### 애플리케이션의 다양한 데이터 저장방법

데이터베이스 : RDBMS, NoSQL 등

파일 : 로컬, 외부 정적 스토리지

캐시서버 : memcached, redis 등



### 데이터베이스와 SQL

데이터베이스의 종류

* RDBMS (관계형 데이터베이스 관리 시스템)

  PostgreSQL, MySQL, SQLite, MS-SQL, Oracle 등

* NoSQL : MongoDB, Cassandra, CouchDB, Google BigTable 등

데이터베이스에 쿼리하기 위한 언어 => SQL

* 같은 작업을 하더라도, 보다 적은 수의 SQL, 보다 높은 성능의 SQL
* 직접 SQL을 만들어내기도 하지만, ORM(Object-relational mapping)을 통해 SQL을 생성/실행하기도 함 => Not Magic.
* 중요) ORM을 쓰더라도, 내가 작성된 ORM코드를 통해 어떤 SQL이 실행되고 있는지 파악하고 이를 최적화할 수 있어야함 -> django-debug-toolbar 활용



### 장고 ORM인 모델은 RDB만을 지원

장고 3.0.2 기준으로 기본 제공되는 backends - mysql, oracle, postgresql, sqlite3

Microsoft SQL Server는 django-pyodbc-azure 라이브러리가 필요



### 다양한 파이썬 ORM (awesome-python#orm)

### Relational Databases

* Django Models, SQLAlchemy, Orator, Peewee, PonyORM 등

#### NoSQL Databases

* django-mongodb-engine, hot-redis, MongoEngine, PynamoDB 등



### 장고의 강점은 Model과 Form

장고에서도 다양한 ORM, 라이브러리 사용 가능

강력한 Model/Form

적절하게 섞어쓸 수 있음

SQL을 직접 실행할 수도 있지만, 가능하면 ORM 쓰기

직접 SQL 문자열 조합하지 말고 인자로 처리 => SQL Injection 방지

`python manage.py shell`

`from django.db import connection`

`cursor = connection.cursor()`

`cursor.close()`

`exit()`



## Django Model

### 장고 내장 ORM

<데이터베이스 테이블>과 <파이썬 클래스>를 1:1로 매핑

모델 클래스명은 단수형으로 지정 - 예: Posts (X), Post (O)

클래스이기에 첫 글자가 대문자인 PascalCase 네이밍

매핑되는 모델 클래스는 DB 테이블 필드 내역이 일치해야함

모델을 만들기 전에, 서비스에 맞게 데이터베이스 설계가 필수

이는 데이터베이스의 영역 -> 관계형 데이터베이스 학습도 필요

파이썬 클래스 정의할 때는 앱 폴더에 models.py에

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



### 모델 활용 순서

장고 모델을 통해, 데이터베이스 형상을 관리할 경우

1. 모델 클래스 작성
2. 모델 클래스로부터 마이그레이션 파일 생성 => makemigrations 명령
3. 마이그레이션 파일을 데이터베이스에 적용 => migrate 명령
4. 모델 활용

장고 외부에서, 데이터베이스 형상을 관리할 경우

* 데이터베이스로부터 모델 클래스 소스 생성 => inspectdb 명령
* 모델 활용



### 모델명과 DB 테이블명

DB 테이블명 : 디폴트 "앱이름_모델명"

예

```
blog앱
* Post 모델 -> "blog_post"
* Comment 모델 -> "blog_comment"

shop 앱
* Item 모델 -> "shop_item"
* Review 모델 -> "shop_review"
```

커스텀 지정

* 모델 Meta 클래스의 db_table 속성

https://docs.djangoproject.com/ko/3.0/ref/models/options/#db-table



### 새로운 모델 만들기

`python manage.py startapp instagram` 

앱 만든 후 settings.py에 INSTALLED_APPS 에 추가

instagram 앱에 urls.py 만들고

```python
urlpatterns = [
]
```

플젝/urls.py에

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
]
```

앱 등록 완료 후

shop/models.py

```python
from django.db import models

class Post(models.Model):
    pass
```

```python
from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

`python manage.py makemigrations instagram`

`python manage.py migrate instagram`

`python manage.py sqlmigrate instagram 0001_initial`  //  실제로 데이터베이스에 들어가는 쿼리를 볼 수 있다



## 적용 순서

Item 모델 정의

마이그레이션 파일 생성 `python manage.py makemigrations 앱이름`

마이그레이션 파일 적용 `python manage.py migrate`

데이터베이스 확인 - DB 종료에 따라 다양한 방법



`python manage.py dbshell`

https://www.sqlite.org/download.html

`.tables`

테이블 목록이 나옴

`.quit`

https://sqliteonline.com 혹은 https://sqlitebrowser.org 에 db.sqlite3 열기





## 장고 모델 필드

### 기본 지원되는 모델필드 타입(1)

Primary Key: AutoField, BigAutoField

문자열: CharField, TextField, SlugField

날짜/시간: DateField, TimeField, DateTimeField, DurationField

참/거짓: BooleanField, NullBooleanField

숫자: IntegerField, SmallIntegerField, PositiveIntegerField, PositiveSmallIntegerfield, BigIntegerField, DecimalField, FloatField

파일: BinaryField, FileField, ImageField, FilePathField

https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types



### 기본 지원되는 모델필드 타입(2)

이메일: EmailField

URL: URLField

UUID: UUIDField

아이피: GenericIPAddressField

Relationship Types

* ForeignKey
* ManyToManyField
* OneToOneField

그리고, 다양한 커스텀 필드들

django-model-utils: https://django-model-utils.readthedocs.io/en/latest/



### 모델필드들은 DB필드타입을 반영

#### DB에서 지원하는 필드들을 반영

* Varchar 필드타입 => CharField, SlugField, URLField, EmailField 등

#### 파이썬 데이터타입과 데이터베이스 데이터타입을 매핑

```
AutoField => int
BinaryField => bytes
BooleanField => bool
CharField/SlugField/URLField/EmailField => str  ==> 디폴트 적용된 유효성 검사 등의 차이
```

#### 같은 모델필드라 할지라도, DB에 따라 다른 타입이 될 수도 있다

DB에 따라 지원하는 기능이 모두 다름



### 자주 쓰는 필드 공통 옵션

blank: 장고 단에서 validation시에 empty 허용 여부 (디폴트: False)

null (DB 옵션): null 허용 여부 (디폴트: False)

db_index (DB 옵션): 인덱스 필드 여부 (디폴트: False)

default: 디폴트 값 지정, 혹은 값을 리턴해줄 함수 지정

* 사용자에게 디폴트값을 제공하고자 할 때

unique (DB 옵션): 현재 테이블 내에서 유일성 여부 (디폴트: False)

choices: select 박스 소스로 사용

validators: validators를 수행할 함수를 다수 지정

* 모델 필드에 따라 고유한 validators들이 등록 (ex- 이메일만 받기)

verbose_name: 필드 레이블, 미지정시 필드명이 사용

help_text: 필드 입력 도움말

```python
# 1:n 에서 n측에다가 외래키 설정
```



#### 설계한 데이터베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해주는 것이, 입력값 오류를 막을 수 있음.

blank/null 지정은 최소화 => manage.py inspect 명령을 통해 생성된 모델 코드는 초안

validators 들이 다양하게/타이트하게 지정됨

필요하다면, validators들을 추가로 타이트하게 지정

프론트엔드에서의 유효성 검사는 사용자 편의를 위해서 수행하며, 백엔드에서의 유효성 검사는 필수

직접 유효성 로직을 만들지 말고 이미 잘 구성된 Features들을 가져다 쓰기

장고의 Form/Model을 통해 지원되며, django-rest-framework의 Serializer를 통해서도 지원됨

#### ORM은 SQL 쿼리를 만들어주는 역할일 뿐, 보다 성능 높은 애플리케이션을 위해서는, 사용하려는 데이터베이스에 대한 깊은 이해가 필요



## 장고 admin을 통한 데이터 관리 (기초)

### django admin

django.contrib.admin 앱을 통해 제공

* 디폴트 경로 : /admin/ => 실제 서비스에서는 다른 주소로 변경 권장(임의의 주소로 정의해도 알아서 찾아감. URL Reverse)
* 혹은 django-admin-honeypot 앱을 통해, 가짜 admin 페이지 노출

모델 클래스 등록을 통해, 조회/추가/수정/삭제 웹UI를 제공

* 서비스 초기에, 관리도구로서 사용하기에 제격
* 관리도구 만들 시간을 줄이고, End-User 서비스에 집중!

내부적으로 Django Form을 적극적으로 사용



### 모델 클래스를 admin에 등록하기

앱/admin.py

```python
from django.contrib import admin
from .models import Item

# 등록법 #1
admin.site.register(Item)  #기본 ModelAdmin으로 동작

#등록법 #2
class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)  # 지정한 ModelAdmin으로 동작

# 등록법 #3
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
```



instagram > admin.py

```python
from django.contrib import admin
from .models import Post

# 등록법 #1
admin.site.register(Post)  #기본 ModelAdmin으로 동작
```

위와 같이 하면 Post 뜸

or

```python
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
```

or

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    pass
```





### 모델 클래스에 `__str__` 구현

admin 모델 리스트에서 "모델명 object"를 원하는 대로 변경하기 위해

객체를 출력할 때, 객체.`__str__()`의 리턴값을 활용

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    
    def __str__(self):
        return f`<{self.pk}> {self.name}`  # str(...)은 자바의 toString()과 유사
```



instagram > models.py

```python
from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message
```



### list_display 속성 정의

모델 리스트에 출력할 컬럼 지정

```python
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    
    def short_desc(self, item):
        return item.desc[:20]
```

instagram > admin.py 에서

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk']
```

이렇게 하면 pk만 나옴.

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_at', 'updated_at']
```

이렇게 하고 저장하면

필드가 나옴

첫번째 column에 링크가 잡혀있음

만약 message에 링크를 잡고 싶으면

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능
```



instagram > models.py

```python
from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message
    
    def message_length(self):  # 인자없는 함수만 가능
        return len(self.message)
```



instagram > admin.py

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능
```



instagram > models.py

```python
def message_length(self):    # 인자없는 함수만 가능
        return len(self.message)
    message_length.short_description = "메세지 글자수"  # 이름도 변경 가능
```

위를 admin단에 구현해보려면 주석처리하고 admin.py 가서

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자"
```



### list_display_links 속성 정의

list_display 지정된 이름 중에, detail 링크를 걸 속성 리스트

```python
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']  # 여러개 가능

    def short_desc(self, item):
        return item.desc[:20]
```



### search_fields 속성 정의

admin내 검색UI를 통해, DB를 통한 where 쿼리 대상 필드 리스트

```python
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']  # 여러개 가능
    search_field = ['name']

    def short_desc(self, item):
        return item.desc[:20]
```



`python manage.py shell`

`from instagram.models import Post`

`Post.objects.all()`

`Post.objects.all().filter(message__icontains='첫번째')`

`qs = Post.objects.all().filter(message__icontains='첫번째')`  // qs로 저장

`print(qs.query)`



instagram > admin.py

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능
    search_fields = ['message']

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자"
```

search_fields = ['message'] 추가

![search](./imgs/1.png)



### list_filter 속성 정의

지정 필드값으로 필터링 옵션 제공

```python
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']  # 여러개 가능
    list_filter = ['is_publish']
    search_field = ['name']

    def short_desc(self, item):
        return item.desc[:20]
```

instagram > admin.py

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능
    list_filter = ['created_at']
    search_fields = ['message']

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자"
```

오른쪽에 필터가 추가됨



instagram > models.py 수정

```python
from django.db import models

class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message
    
    # admin단에 구현도 가능함
    # def message_length(self):    # 인자없는 함수만 가능
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"  # 이름도 변경 가능
```

exit()  빠져나오기

`python manage.py makemigrations instagram`

migrations 폴더에 0002 파일 생성됨

`python manage.py migrate instagram`  // 실제 db에 적용

`python manage.py showmigrations instagram`  // 적용 내역

`python manage.py showmigrations`  // 앱 이름 없이하면 전체 



instagram > admin.py 에 'is_public' 추가

```python
list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
```

필터에도 추가

```python
list_filter = ['created_at', 'is_public']
```

