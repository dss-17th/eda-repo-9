# KoreaMovie_EDA

<img src ='https://postfiles.pstatic.net/MjAyMTA0MjBfMjY2/MDAxNjE4OTE2OTgwMTI3.-gONCwJ7vU1OHudwPJDTAg4VAGq8VzkdoENmuan2rXgg.yUD9Xtxp8FaJbsjNf63gPAphyRutRq0RP0KXXwa71x8g.JPEG.greatsol98/KakaoTalk_Photo_2021-04-18-19-56-22.jpeg?type=w966' width='300' >

- 극장 뿐만 아니라 OTT 서비스에서도 독립/예술 영화 서비스 경쟁 진행 중
- 이는 지난 십년 동안 한국에서도 독립 영화 시장이 커져갔고 이에 따라 ‘영화’ 라는 단어의 의미 확장이 진행되었다고 생각

- 전체적인 영화 산업에 대한 분석 진행 
- 추가적으로 일반영화와 독립/예술영화을기준으로 분류하여 비교 분석


## 데이터 소개
* * *

<img src = 'https://postfiles.pstatic.net/MjAyMTA0MjBfMjcg/MDAxNjE4OTI1MzM1NDQ5.1ycZuuuOgnXxm3xfIgNEObKuHgBdWb_JYLYlTBz_HKMg.hFEzo5R39BQ37r6C5w8VLVGcHn8kMJgPhjHjodPtrQEg.PNG.greatsol98/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2021-04-18_%EC%98%A4%ED%9B%84_8.01.22.png?type=w966'>

- 2011년 1월 부터 2021년 4월 9일까지 개봉한 전체 영화 일람 데이터 

> **출처 : 한국영화진흥위원회 박스오피스 https://www.kofic.or.kr/kofic/business/infm/introBoxOffice.do**

## 결론
----

- 1. 독립/예술 영화 배급사는 일반 영화에 비해 현저하게 적으며 이러한 문제때문에 일반 영화가 4개의 작품이 개봉할 때 독립/예술 영화는 1개의 작품만 개봉된 다는 것을 알 수 있다.
- 2.	2018년부터 독립/예술 영화의 지속적인 감소세가 보이고 있었으며 2019년에는 예년 수준으로 잠시 회복했으나 2020년 코로나로 인하여 다시 또 하락하고 있다.
- 3.	전체 개봉 영화 중에는 청소년 관람불가 작품이 많고 장르적으로는 독립/예술 영화는 다큐멘터리, 일반 영화는 멜로/로맨스 작품이 가장 많은 분포를 가지고 있다. 특이하게 일반영화에서는 성인물 작품 수가 많다. 
- 4.	매출액이 높은 영화의 장르는 드라마, 범죄, 사극 순으로 많이 분포하였고 12세와 15세이상 관람가 작품이 많았다. 그러나 장르와 등급의 상관관계에서는 액션과 15세이상 관람가, 액션과 12세이상 관람가, 애니메이션과 전체관람가가 가장 유의미하게 상관이 있다는 결과가 나왔다. 
- 5.	독립/예술 영화의 서울 관객수와 전국 관객수는 크게 차이가 나지 않는데 이것은 독립영화관이 주로 서울에 집중이 되어 있어서 그렇다. 매출액 기준으로 전국과 서울 지역의 독립/예술 영화 상위 5위권 영화는 차이가 거의 없는데 일반 영화에서는 유독 서울 지역에서 외국 영화가 상위에 랭크 되어 있다는 것을 알 수 있다. 이것 또한 지방은 영화관 인프라가 부족해서 다양한 영화를 접할 수 없기 때문이다.
- 6.	유독 멜로/로맨스 작품에 청소년 관람불가 작품이 많았던 이유는 실제적으로는 성인물(에로) 작품이 멜로/로맨스 장르로 구분되어 있기 때문이었다. 이런 영화들은 주로 스크린수가 1개로 잡혀있는데 이것을 “형식 개봉 영화” 라고 하고 한국과 일본 국적을 가진 영화가 가장 많았다. 
- 7.	영화 제목은 관객이 마주하는 첫 요소로 영화에 대한 흥미를 불러일으키는 가장 직접적인 요소중 하나이다. 이런 영화 제목은 관객의 감성을 자극해 영화에 호소력을 더하는 호소적 기능과 함께 언어의 수사적 기교를 통해서 관객의 심금을 울리는 심미적 기능이 있다고 알려져 있습니다.* 워드 클라우드의 결과는 국내 독립/예술 영화는 관객들에게 감성적으로 어필을 하고 있다는 것을 알 수 있습니다.

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>

</head>
<body>
    <div id="fcfa1fd551944cabb9ce125095db97ae" class="chart-container" style="width:1350px; height:750px;"></div>
    <script>
        var chart_fcfa1fd551944cabb9ce125095db97ae = echarts.init(
            document.getElementById('fcfa1fd551944cabb9ce125095db97ae'), 'white', {renderer: 'canvas'});
        var option_fcfa1fd551944cabb9ce125095db97ae = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#802200",
        "#B33000",
        "#FF4500",
        "#FAA327",
        "#9ECB3C",
        "#6DBC49",
        "#37B44E",
        "#14ADCF",
        "#209AC9",
        "#1E91CA"
    ],
    "series": [
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\uc77c\ubcf8",
                    "value": 48.0
                },
                {
                    "name": "\ud55c\uad6d",
                    "value": 23.61
                },
                {
                    "name": "\ubbf8\uad6d",
                    "value": 15.15
                },
                {
                    "name": "\uc601\uad6d",
                    "value": 1.82
                },
                {
                    "name": "\ud504\ub791\uc2a4",
                    "value": 1.77
                },
                {
                    "name": "\uc911\uad6d",
                    "value": 1.18
                },
                {
                    "name": "\uce90\ub098\ub2e4",
                    "value": 1.07
                },
                {
                    "name": "\ud64d\ucf69",
                    "value": 0.97
                },
                {
                    "name": "\ub3c5\uc77c",
                    "value": 0.86
                },
                {
                    "name": "\ub7ec\uc2dc\uc544",
                    "value": 0.62
                }
            ],
            "radius": [
                "20%",
                "95%"
            ],
            "center": [
                "30%",
                "60%"
            ],
            "roseType": "area",
            "label": {
                "show": true,
                "position": "inside",
                "margin": 8,
                "fontSize": 12,
                "fontStyle": "italic",
                "fontWeight": "bold",
                "fontFamily": "Century",
                "formatter": "{b}:{c}%"
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\uc77c\ubcf8",
                "\ud55c\uad6d",
                "\ubbf8\uad6d",
                "\uc601\uad6d",
                "\ud504\ub791\uc2a4",
                "\uc911\uad6d",
                "\uce90\ub098\ub2e4",
                "\ud64d\ucf69",
                "\ub3c5\uc77c",
                "\ub7ec\uc2dc\uc544"
            ],
            "selected": {},
            "show": false,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "title": [
        {
            "text": "\uc2a4\ud06c\ub9b0\uc218 1\uac1c\uc778 \uc601\ud654\uc758 \uad6d\uc801 \ubd84\ud3ec",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "type": "png",
                "backgroundColor": "auto",
                "connectedBackgroundColor": "#fff",
                "show": true,
                "title": "\u4fdd\u5b58\u4e3a\u56fe\u7247",
                "pixelRatio": 1
            },
            "restore": {
                "show": true,
                "title": "\u8fd8\u539f"
            },
            "dataView": {
                "show": true,
                "title": "\u6570\u636e\u89c6\u56fe",
                "readOnly": false,
                "lang": [
                    "\u6570\u636e\u89c6\u56fe",
                    "\u5173\u95ed",
                    "\u5237\u65b0"
                ],
                "backgroundColor": "#fff",
                "textareaColor": "#fff",
                "textareaBorderColor": "#333",
                "textColor": "#000",
                "buttonColor": "#c23531",
                "buttonTextColor": "#fff"
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "\u533a\u57df\u7f29\u653e",
                    "back": "\u533a\u57df\u7f29\u653e\u8fd8\u539f"
                },
                "icon": {},
                "xAxisIndex": false,
                "yAxisIndex": false,
                "filterMode": "filter"
            },
            "magicType": {
                "show": true,
                "type": [
                    "line",
                    "bar",
                    "stack",
                    "tiled"
                ],
                "title": {
                    "line": "\u5207\u6362\u4e3a\u6298\u7ebf\u56fe",
                    "bar": "\u5207\u6362\u4e3a\u67f1\u72b6\u56fe",
                    "stack": "\u5207\u6362\u4e3a\u5806\u53e0",
                    "tiled": "\u5207\u6362\u4e3a\u5e73\u94fa"
                },
                "icon": {}
            },
            "brush": {
                "icon": {},
                "title": {
                    "rect": "\u77e9\u5f62\u9009\u62e9",
                    "polygon": "\u5708\u9009",
                    "lineX": "\u6a2a\u5411\u9009\u62e9",
                    "lineY": "\u7eb5\u5411\u9009\u62e9",
                    "keep": "\u4fdd\u6301\u9009\u62e9",
                    "clear": "\u6e05\u9664\u9009\u62e9"
                }
            }
        }
    }
};
        chart_fcfa1fd551944cabb9ce125095db97ae.setOption(option_fcfa1fd551944cabb9ce125095db97ae);
    </script>
</body>
</html>


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