### 웹 프론트엔드를 위한 3가지 언어

* HTML (Hyper Text Markup Language) : 웹페이지의 내용 및 구조. 
* CSS (Cascasding Style Sheet) : 웹페이지의 스타일
* JavaScript : 웹페이지의 로직

위 세 언어는 모든 웹브라우저에서 거의 유사하게 동작

여러 버전의 HTML/CSS/JavaScript가 있으며, 브라우저마다 지원하는/구현된 Features가 다를 수도 있음



1) 한 HTML 파일에 CSS/Javascript를 모두 넣기도 하며

cf) 개발자도구 - Network

2) 대개 별도 CSS/JavaScript 파일로 분리



### CSS/JavaScript 파일을 별도 파일로 분리하는 이유

1. HTML 응답 body 크기를 줄일 수 있음
2. 여러 번 새로고침하더라도, 브라우저 캐싱기능을 통해 같은 파일을 서버로부터 다시 읽어들이지 않음
3. 웹페이지 응답성을 높여줄 수 있음



### CSS/JavaScript의 슈퍼셋 언어

CSS 소스코드

* 처음에는 직접 CSS 날코딩을 하고,
* 추후에는 성향에 따라 Sass, Less 검토
  * sass. less 문법으로 작성된 코드를 빌드하여, css파일을 만들어냄

JavaScript

* 처음에는 직접 JavaScript 날코딩을 하고
* 추후에는 성향에 따라 TypeScript 검토
  * TypeScript 문법으로 작성되는 코드를 빌드하여, javascript 파일을 만들어냄



## 웹 프론트엔드와 백엔드

웹개발은 크게 백엔드와 프론트엔드 개발로 나눠짐.

장고는 백엔드에 초점이 맞춰진 웹프레임워크

장고를 공부할 땐 백엔드에 포커스를 맞춰서 공부하고,

웹프론트엔드는 최소화

* 백엔드 먼저. Android/iOS 앱 X
* 웹서비스 점진적으로 개선



### 개발 언어

프론트엔드 개발언어 (여러 클라이언트 단 중 하나)

* 브라우저 단에서 실행이 됨
* HTML/CSS/JavaScript의 조합

cf) 보통의 브라우저, CLI 전용 브라우저, Android/iOS앱 등 HTTP 요청을 보낼 수 있는 어떠한 프로그램이든지, 클라이언트가 될 수 있음

백엔드 개발언어 (서버 단)

* 클라이언트 단의 요청을 처리/응답만 할 수 있으면 됨
* 다양한 언어가 가능하며, 여러 언어/프레임워크를 섞어쓸 수도 있음 (Python, NodeJS, Ruby, Java 등)



### 웹 요청 및 응답[                   리액트와 함께 장고 시작하기 Complete (슬라이드 PDF 제공)                  ](https://educast.com/course/web/ZU53)

* 웹은 HTTP(S) 프로토콜로 동작함
* 하나의 요청은 클라이언트가 웹서버로 요청하며, 웹서버는 요청에 맞게 응답을 해야함
  - 응답은 HTML 코드 문자열, CSS 코드 문자열, JavaScript 코드 문자열, Zip, MP4 등 어떠한 포맷이라도 가능함
* 웹서버에서 응답을 만들 때, 요청의 종류를 구분하는 기준
  * URL (일반적), 요청헤더, 세션, 쿠키 등
* 웹서버 구성에 따라
  * /static/flower.jpg : JPG파일 내용을 응답으로 내어주도록 설정했음
  * /blog/images/flower.jpg : 장고 View를 통해, JPG파일 내용을 응답으로 내어주도록 설정
  * /blog/images/flower/ : 장고 View를 통해, JPG파일 내용을 응답으로 내어주도록 설정
* 웹서버 구성에 따라, 특정 요청에 대한 응답을 Apache/Nginx 웹서버에도 할 수 있고 Django뷰에서 응답을 할 수도 있음



## 일반적인 장고 페이지의 예

### 뷰 : 포스팅 목록

```python
# blog/urls.py 
from django.urls import path 
from . import views

urlpatterns = [ 
    path('blog/', views.post_list, name='post_list'), 
]

# blog/views.py 
from django.shortcuts import render 
from .models import Post

def post_list(request): 
    return render(request, 'blog/post_list.html', { 
        'post_list': Post.objects.all(), 
    })
```



### HTML 템플릿

```html
<!doctype html> 
<html> 
    <head> 
        <meta charset="utf-8" /> 
        <title>AskDjango Blog</title> 
    </head> 
    <body> 
        <h1>AskDjango Blog</h1> 
        <ul> 
            {% for post in post_list %} 
            	<li> 
                    {{ post.title }} 
            	</li> 
            {% endfor %} 
        </ul> 
        <hr/> 
        &copy; 2019, AskDjango. 
    </body> 
</html>
```



### 단지 하나의 HTTP 요청에 대해, 하나의 응답을 받음

1. 브라우저에서 서버로 HTTP 요청 
2. 서버에서는 해당 HTTP요청에 대한 처리 : 장고에서는 관련 뷰 함수가 호출 
3. 뷰 함수에서 리턴해야만 비로소 HTTP응답이 시작되며, 그 HTTP 응답을 받기 전까지는 하얀 화면만 보여짐. 따라서 뷰 처리시간이 길어질수록 긴? 화면이 보여지는 시간이 길어진다. 
4. 브라우저는 서버로부터 HTTP 문자열 응답을 1줄씩 해석하여, 그래픽적으로 표현

cf) 아직, HTML 문자열 응답에 추가 리소스 (CSS, JavaScript, Image 등)가 없음



### 만약 HTML 문자열 응답에 추가 리소스가 지정되어있다면?

```html
<!doctype html> 
<html> 
    <head> 
        <meta charset="utf-8" /> 
        <title>AskDjango Blog</title> 
        <link rel="stylesheet" href="/static/style.css" /> 
        <script src="/static/jquery-3.2.1.min.js"></script> 
    </head> 
    <body> 
        <h1>Ask Django Blog</h1> 
        <ul> 
            {% for post in post_list %} 
            	<li> 
                    {{ post.title }} 
            	</li> 
            {% endfor %} 
        </ul> 
        <hr/> 
        &copy; 2019, Ask Company. 
    </body> 
</html>
```

HTML 문자열은 1줄씩 처리되며, 외부 리소스는 해당 리소스가 로딩완료/실행될 때까지 대기함



### HTML UI 응답성이 낮아지는 경우

과도한 JavaScript 로딩 및 계산 

과도한 CSS 레이아웃 로딩 및 계산 

잦은 시각적 개체 업데이트



### HTML UI 응답성을 높이기 위해

* #### 실서비스시에 CSS/JavaScript파일은 Minify시켜서 다운로드 용량 줄이기

* #### 대개 CSS를 HTML컨텐츠보다 앞에 위치시키고 

  * CSS가 컨텐츠보다 뒤에 위치한다면, 유저에게는 스타일이 적용되지 않은 HTML컨텐츠가 먼저 노출될 수 있음

* #### JS를 HTML컨텐츠보다 뒤에 위치

  * JS는 스타일에 직접적인 영향을 끼치지 않기 때문에, HTML컨텐츠보다 나중에 로딩되어도 대개 괜찮음
  * 꼭 필요한 몇몇 JS는 HTML컨텐츠보다 앞에 위치시키기도 함



구글맵이 나오면서부터, 

### 문서의 시대 => 웹 애플리케이션의 세계 OPEN 

* 표준 웹기술만으로 웹문서에서 탈피하여, 웹 애플리케이션
  * 웹 애플리케이션에서는 복잡한 UI 처리가 필요하므로, React/Vue/Angular 등을 많이 사용 

* 표준 웹기술만으로 지도 서비스가 가능. 이전에는 ActiveX 혹은 Flash를 통해서만 구현가능





## CSS Layout

### CSS (Cascading Style Sheets)

각 HTML 엘리먼트에 대한 스타일을 기술
MSN 웹 문서 : https://developer.mozilla.org/ko/docs/Web/CSS 

https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps

https://developer.mozilla.org/ko/docs/Learn/CSS

https://developer.mozilla.org/ko/docs/Learn/CSS



Table 기반의 레이아웃이 흥하던 시절
HTML로 문서의 구조를, CSS로 스타일링을 한다는 개념이 보급되기 전에는 <table>태그로 레이아웃을 잡았다. 

Table for Layout은 직관적인 레이아웃이지만, 웹표준 방식에 맞지 않다.

CSS Layout 방식은? 

* 코드 용량 절감
* 사람이나 컴퓨터가 이해하기 쉬운 구조
* 쉬운 유지보수

 웹 표준 코딩의 장점, Table for Layout과 CSS Layout의 비교실험 



### CSS 러닝커브

### 반응형 웹 <- 브라우저의 가로크기에 따라 각기 다른 CSS 스타일을 적용 (다른 레이아웃을 적용) 되는 웹페이지 

### CSS Media Queries를 통해 구현 

```css
/* 브라우저의 가로크기가 600px 이하일 경우, 아래 스타일이 적용 */ @media (max-width: 600px) { 
    body { 
        background-color: green; 
    } 
}
```

https://developer.mozilla.org/ko/docs/Web/Guide/CSS/Media_queries



### 반응형 웹의 단점

예전에는 모바일/데스크탑 페이지를 따로 만드는 경우도 많았으나, 반응형 웹으로 구현하면 한 페이지에서 모바일/데스크탑 페이지를 한 페이지에서 대응 가능 

모든 해상도 대응을 위한 CSS/이미지를 모두 불러와야 하므로, 로딩 시간 길어짐 

복잡한 컨텐츠에는 맞지 않을 수도 있다(레이아웃과 컨텐츠가 복잡하지 않아야, 일관된 UX 제공 가능) 

따로 분리하는 것이 더 나은 선택일 수도
네이버는 모바일페이지 https://m.naver.com 와 데스크탑페이지 https://naver.com 가 분리 

Adaptive Web (적응형 웹) : 특정 디바이스/해상도를 정해두고, 그에 맞춰 웹페이지를 구성하는 방식



기술이 중요한 것이 아니라
유지보수하기 좋고, 사용자가 이용하기 좋도록 

사용자는 반응형/적응형 웹이든 모바일/데스크탑 기기에서의 사용이 편리하면 OK 유저가 사용하기 편리해야 



## CSS Framework

초기 구성의 용이함 

기본적인 CSS스타일을 이미 구성 

이미 일정 수준의 작업이 되어있기에, 원하는 레이아웃으로 작업해서 초기 웹페이지를 구성하기에 편리 

하지만, 같은 CSS Frameworks를 쓴 사이트는 같은 서비스인 것처럼 보여짐

구성하기 나름. CSS Frameworks 만으로 끝나지 않음. 시작은 쉽게 하되, 좋은 디자인을 뽑아내기 위해서는 커스텀이 필요한 시점이 옴.
기본이 잘 갖춰져있기에 커스텀하기도 용이하며 레퍼런스가 많음. 좋은 퀄리티의 유료테마까지 



## Best CSS Frameworks of 2019

1. Bootstrap  
2. Materialize CSS
3. Semantic UI
4. Material UI 
5. UIKit 
6. Foundation

### 가장 레퍼런스가 많은 Bootstrap4

+ 기본 스타일도 좋고 
+ 반응형도 잘 지원하고 
+ Bootstrap4에서의 다양한 무료/유료 테마



## CDN

최적화된 전세계적으로 촘촘히 분산된 서버로 이루어진 플랫폼 

전 세계의 유저에게 빠르고 안전한 정적파일 전송

우리는 하나의 원본(Origin)서버를 가지고, 

CDN 서비스 업체에서는 전 세계에 걸쳐 컨텐츠 서버를 가지고 있고, 

원본 서버로부터 각 컨텐츠 서버로 데이터를 복제

전 세계의 유저들이 동일한 주소로 컨텐츠를 요청을 하면, 

CDN 서비스에서는 이 요청을 해당 유저와 물리적으로 가까운 CDN 콘텐츠 서버에서 응답토록 구성
https://www.akamai.com/kr/ko/cdn/what-is-a-cdn.jsp

추천 강의) 게임 개발을 위해 알아야할 Azure CDN



### 다양한 Bootstrap4, Free 템플릿

https://bootswatch.com/ 

https://colorlib.com/wp/free-bootstrap-4-website-templates/



### 장고 프로젝트에 Bootstrap4 및 커스텀 테마를 적용해보기