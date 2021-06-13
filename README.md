# KoreaMovie_EDA

- 극장 뿐만 아니라 OTT 서비스에서도 독립/예술 영화 서비스 경쟁 진행 중
- 이는 지난 십년 동안 한국에서도 독립 영화 시장이 커져갔고 이에 따라 ‘영화’ 라는 단어의 의미 확장이 진행되었다고 생각

- 전체적인 영화 산업에 대한 분석 진행 
- 추가적으로 일반영화와 독립/예술영화을기준으로 분류하여 비교 분석



## 데이터 소개
<p align="center">
<img src = 'https://postfiles.pstatic.net/MjAyMTA0MjBfMjcg/MDAxNjE4OTI1MzM1NDQ5.1ycZuuuOgnXxm3xfIgNEObKuHgBdWb_JYLYlTBz_HKMg.hFEzo5R39BQ37r6C5w8VLVGcHn8kMJgPhjHjodPtrQEg.PNG.greatsol98/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2021-04-18_%EC%98%A4%ED%9B%84_8.01.22.png?type=w966' width='700'></p>

- 2011년 1월 부터 2021년 4월 9일까지 개봉한 전체 영화 일람 데이터 

> **출처 : 한국영화진흥위원회 박스오피스 https://www.kofic.or.kr/kofic/business/infm/introBoxOffice.do**

## 결론
----

![작품수(영화구분)](https://user-images.githubusercontent.com/75258999/121805557-b4723680-cc86-11eb-901f-3d0f2e269e76.png)
- 일반 영화가 4개의 작품이 개봉할 때 독립/예술 영화는 1개의 작품만 개봉

![개봉작품수(영화구분)](https://user-images.githubusercontent.com/75258999/121805569-ba681780-cc86-11eb-89cc-7f4a56ff8573.png)
- 2018년부터 독립/예술 영화의 지속적인 감소세가 보이고 있었으며 2019년에는 예년 수준으로 잠시 회복했으나 2020년 코로나로 인하여 다시 또 하락

![등급분포(영화구분)](https://user-images.githubusercontent.com/75258999/121805579-c2c05280-cc86-11eb-8d2b-c0a4c66afc51.png) ![장르분포](https://user-images.githubusercontent.com/75258999/121805594-cbb12400-cc86-11eb-8cdf-abecbf1691ef.png) ![멜로,로멘스영화-등급분포](https://user-images.githubusercontent.com/75258999/121805598-d10e6e80-cc86-11eb-8b35-9009f2eee2cb.png)
- 전체 개봉 영화 중에는 청소년 관람불가 작품이 많고 장르적으로는 독립/예술 영화는 다큐멘터리, 일반 영화는 멜로/로맨스 작품이 가장 많은 분포를 가지고 있다. 특이하게 일반영화에서는 성인물 작품 수가 많다. 

![top100(장르분포)](https://user-images.githubusercontent.com/75258999/121805610-da97d680-cc86-11eb-8bf5-4f736a4b0fc4.png)
![top100(등급분포)](https://user-images.githubusercontent.com/75258999/121805612-dbc90380-cc86-11eb-961e-0cacaf121ac7.png)
![장르-매출액(상관관계)](https://user-images.githubusercontent.com/75258999/121805618-e5526b80-cc86-11eb-86ed-7a89d5e49373.png)
- 매출액이 높은 영화의 장르는 드라마, 범죄, 사극 순으로 많이 분포하였고 12세와 15세이상 관람가 작품이 많았다. 그러나 장르와 등급의 상관관계에서는 액션과 15세이상 관람가, 액션과 12세이상 관람가, 애니메이션과 전체관람가가 가장 유의미하게 상관이 있다는 결과가 나왔다. 

![관객수-분포(지역)](https://user-images.githubusercontent.com/75258999/121805624-e97e8900-cc86-11eb-8a77-da86b0f286ff.png)
- 독립/예술 영화의 서울 관객수와 전국 관객수는 크게 차이가 나지 않는데 이것은 독립영화관이 주로 서울에 집중이 되어 있어서 그렇다. 매출액 기준으로 전국과 서울 지역의 독립/예술 영화 상위 5위권 영화는 차이가 거의 없는데 일반 영화에서는 유독 서울 지역에서 외국 영화가 상위에 랭크 되어 있다는 것을 알 수 있다. 이것 또한 지방은 영화관 인프라가 부족해서 다양한 영화를 접할 수 없기 때문이다.

<img width="476" alt="rosechart1" src="https://user-images.githubusercontent.com/75258999/121805655-fa2eff00-cc86-11eb-82ed-a23eed7ed905.png">
<img width="453" alt="rosechart2" src="https://user-images.githubusercontent.com/75258999/121805658-fbf8c280-cc86-11eb-868e-3631a93406bc.png">
- 유독 멜로/로맨스 작품에 청소년 관람불가 작품이 많았던 이유는 실제적으로는 성인물(에로) 작품이 멜로/로맨스 장르로 구분되어 있기 때문이었다. 이런 영화들은 주로 스크린수가 1개로 잡혀있는데 이것을 “형식 개봉 영화” 라고 하고 한국과 일본 국적을 가진 영화가 가장 많았다. 

![wordcount](https://user-images.githubusercontent.com/75258999/121805660-01560d00-cc87-11eb-8d58-7f4cc8da9033.png)
![wordcloud](https://user-images.githubusercontent.com/75258999/121805664-03b86700-cc87-11eb-827b-eaee7a25439d.png)
- 영화 제목은 관객이 마주하는 첫 요소로 영화에 대한 흥미를 불러일으키는 가장 직접적인 요소중 하나이다. 이런 영화 제목은 관객의 감성을 자극해 영화에 호소력을 더하는 호소적 기능과 함께 언어의 수사적 기교를 통해서 관객의 심금을 울리는 심미적 기능이 있다고 알려져 있습니다.* 워드 클라우드의 결과는 국내 독립/예술 영화는 관객들에게 감성적으로 어필을 하고 있다는 것을 알 수 있습니다.



## 과정
----
- 모듈
> - rate.py : 영화 등급 분류

<img src ='https://postfiles.pstatic.net/MjAyMTA0MjBfNTcg/MDAxNjE4OTI2Mjc2NDk4.CPVi8k_VRC_K296mTCFMcKwAMhext4GEvAlRdU3htrYg.NwslRAo0A0qvIY95SXM2K8sStzjlSEgyOveNnJH2qwsg.PNG.greatsol98/rate.png?type=w966'>

> - wordcount.py : 가장 많이 사용된 20개의 단어 추출

<img src = 'https://postfiles.pstatic.net/MjAyMTA0MjBfNzMg/MDAxNjE4OTI2Mjc2MjEy.jWPEqqvz9mkC03BdX4e4MGq6EWhqJOeYXHYjK-cVWUcg.1drQ_DQny32hBPFGb4Xq0xQBbGmKKbQwXP0KyTHr13Eg.PNG.greatsol98/wordcount.png?type=w966'>

## 개선사항
----
- 아웃라이어 제거 후 EDA 진행


## 참고
----

- <독립 영화에 대한 현실적인 고민> 부산일보 : http://weekly.pusan.ac.kr/news/articleView.html?idxno=10499
- <절반으로 뚝 떨어진 독립영화 관객... 한국영화의 '위기'> 오마이뉴스 : http://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0002512932&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news
- <서울 사람들이 지방 사람들보다 외국영화를 더 좋아한다고?> 경향신문 : https://www.khan.co.kr/culture/movie/article/201310141616491#csidx8d78a29a592e1c4bdd413f232e29a8e
- <영화 제목으로 본 영한 번역기법 연구: 영화 산업 정책과 언어 정책의 변화를 중심으로> 권유진, 2020
