## 다양한 개발 파트



웹 프론트엔드 개발

```
웹 브라우저에서 구동되는 애플리케이션을 개발.
HTML/CSS/JavaScript를 기반으로 다수의 언어/라이브러리
ex) React.js, Vue.js, Angular, jQuery, Bootstrap 등
```



스마트폰 애플리케이션 개발

```
Android/iOS 스마트폰/타블렛에서 구동되는 
애플리케이션을 Java/Swift/Objective-c 언어로 개발.
앱에 웹브라우저를 임베딩하여 웹 프론트엔드 기술로 앱을 개발하기도 함
```



============================================================================



인프라 관리

```
자체 서버, 서버/웹 호스팅, AWS/Azure/Google/Heroku 클라우드 (laaS와 PaaS) 등

백엔드 개발
- Django, Flask, Spring (Java), Ruby on Rails (Ruby) 등
```





### 웹프레임워크가 왜 필요한가요?

우선 웹서비스가 왜 필요한가요?

* 서버의 역할

  모든 서비스의 근간

  어떤 서비스든 웹서비스든 당연히 잘해야하는 분야.

  카카오톡/트위터 <- Ruby on Rails 로 웹베이스에서 API를 제공했었음

만들 수 있는 것

* 웹서비스, 앱 서버, 챗봇 서비스 등등

웹서비스를 만들때마다 반복되는 것들을 표준화해서 묶어놓음.

* 거의 모든 언어마다 웹프레임워크가 존재





## 다양한 파이썬 웹프레임워크

* Django : The Web framework for perfectionists with deadlines.

  백엔드 개발에 필요한 거의 모든 기능을 제공

  중복된 작업을 최대한 줄여주는 최고의 웹 프레임워크

* Flask : a micro framework for Python based on Werkzeug.

  백엔드 개발에 필요한 일부분의 기능을 제공

  ORM으로서 SQLAlchemy를 주로 사용

* Sanic : Async Python 3.5+ web server/framework

* Tornado : asynchronous networking library 등등

https://wiki.python.org/moin/WebFrameworks



## Django의 강점

1. Python 생태계
   * 크롤링, 자동화, 머신러닝 코드와 같은 언어
   * 표현력이 좋고, 가독성 높은 코드
2. 건강한 커뮤니티
3. 풀스택 웹프레임워크
   * 백엔드 개발에 필요한 거의 모든 것을 Django에서 직접 지원
     * API 개발에 필요한 거의 모든 것을 django-rest-framework에서 지원
   * 참고) 프론트엔드 개발에서의 요즘 트렌드는 React, Vue, Angular
4. 10년동안 충분히 성숙
   * 2008년에 1.0 공개, 2019년 12월에 3.0 공개



## Django

기타리스트 Django Reinhardt 이름을 딴 작명

Lawrence Journal-World 신문사에서 2003년부터 개발, 2005년에 세상에 공개

2008년에 1.0 릴리즈

장고 3.x부터 비동기 지원 시작

github.com/django/django



## 장고는 MTV 프레임워크

이름만 다를 뿐, MVC

* Model -> 장고의 Model

  데이터베이스 SQL 쿼리를 생성/수행 ORM

* View -> 장고의 Template

  복잡한 문자열 조합을 도와줌

* Controller -> 장고의 View

  HTTP 클라이언트로부터의 요청을 처리하는 함수



### 백엔드는 서비스의 중심

백엔드/서비스운영을 먼저 탄탄하게 하고 나서, 프론트/앱을 고민



웹 서비스 및 API : 파이썬/장고

웹 프론트엔드: 리액트와 jQuery

인프라: PaaS (Platform as a Service) 혹은 Serverless 플랫폼