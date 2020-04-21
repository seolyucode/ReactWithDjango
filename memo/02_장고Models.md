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