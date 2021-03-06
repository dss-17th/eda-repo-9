# '등급' 총 5가지로 나눔 (전체관람가(G), 12세이상관람가(pg), 15세이상관람가(pg13), 청소년관람불가(r), 제한상영가(nc17))
def rating (row):
    G = ['전체관람가','연소자관람가,전체관람가', '연소자관람가', '모든 관람객이 관람할 수 있는 등급', "모든 관람객이 관람할 수 있는 등급,전체관람가"]
    pg = ['12세이상관람가', '12세관람가', '중학생이상관람가', '국민학생관람불가', '12세이상관람가,12세관람가', '12세 미만인 자는 관람할 수 없는 등급', '12세이상관람가,전체관람가', '12세이상관람가,중학생이상관람가', 
          '12세이상관람가,연소자관람가', '12세이상관람가,국민학생관람불가', '12세이상관람가,연소자관람가,전체관람가']
    pg13 = ['15세이상관람가', '15세관람가', '고등학생이상관람가', '15세 미만인 자는 관람할 수 없는 등급', '15세관람가,15세이상관람가', '15세이상관람가,중학생이상관람가', '연소자관람불가,15세이상관람가', '국민학생관람불가,15세이상관람가',
           '15세이상관람가,전체관람가', '연소자관람가,15세이상관람가', '12세이상관람가,15세이상관람가','15세 미만인 자는 관람할 수 없는 등급 ,15세이상관람가',
           '12세이상관람가,국민학생관람불가,15세이상관람가','12세이상관람가,고등학생이상관람가', '15세관람가,12세이상관람가', '12세이상관람가,15세 미만인 자는 관람할 수 없는 등급']
    r = ['청소년관람불가', '18세관람가', '연소자관람불가', '18세 미만인 자는 관람할 수 없는 등급', '고등학생이상관람가,15세이상관람가', 
         '연소자관람불가,청소년관람불가', '미성년자관람불가', '18세관람가,청소년관람불가', '청소년관람불가,15세이상관람가', '15세이상관람가,18세 미만인 자는 관람할 수 없는 등급','미성년자관람가',
        '청소년관람불가,전체관람가', '청소년관람불가,12세관람가', '15세이상관람가,미성년자관람불가', '국민학생관람불가,청소년관람불가',
        '18세관람가,15세이상관람가', '청소년관람불가,고등학생이상관람가']
    nc17 = ['제한상영가']
    none = ['정보없음']
    
    if row in G :
        return '전체관람가'
    if row in pg :
        return '12세이상'
    if row in pg13 :
        return '15세이상'
    if row in r :
        return '청소년관람불가'
    if row in nc17:
        return '제한상영가'
    if row in none:
        return '정보없음'