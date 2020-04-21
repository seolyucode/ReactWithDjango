### 패러다임의 전환: "웹 문서 -> 웹 애플리케이션"



## SPA (Single Page Application) 개발 방법론

웹 문서의 기본 동작에서는 화면 전환 시에

1. 서버로부터 새로운 화면에 대한 HTML/CSS/JavaScript를 받아와서
2. 전체 화면을 새로 그린다

=> 웹 문서에 적합한 방식



SPA 방식의 화면 전환

1. JavaScript를 통해 화면을 변경 -> 화면 전환 느낌이 나도록
2. 필요 시에 백그라운드에서 JavaScript로 서버와 통신

=> 웹 애플리케이션에 적합한 방식



jQuery로도 웹 애플리케이션 만들 수 있지만 SPA 방식의 애플리케이션을 만들 수 있도록 도와주는 라이브러리(리액트, VUe.js, 앵귤러..) 활용



## React

사용자 인터페이스를 만들기 위한 JavaScript 라이브러리



### 다양한 자바스크립트 런타임

거의 모든 웹브라우저에서 HTML/CSS/JavaScript 지원

* 웹 브라우저 단에서 구동
* 웹 브라우저/버전마다 지원하는 JavaScript Spec이 상이

데스크탑에서는 NodeJS 활용

* 데스크탑/서버 단 개발이 가능
* 윈도우에서의 Microsoft의 전폭적인 지지

nodejs로 구동되는 간단 웹서버

```nodejs
'use strict';

const http = require('http');
const port = process.env.PORT || 8888;

http.createServer((req, res)) => {
	res.writeHead(200, {'Content-Type': 'text/plain'};
	res.end('Hello World : ');
}).listen(port);
```



### 다양한 자바스크립트 버전

ES3 (1999)

ES5 (2009)

---------------------------------------------

ES6 (2015) -> git.io/es6features

ES7 (2016)

ES8 (2017) : async/await 지원

ES9 (2018) : object rest/spread 지원

ES10 (2019)