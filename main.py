# Module Load
import warnings
warnings.filterwarnings(action='ignore')

from module.Font import Fontmanager
path = Fontmanager()

import pandas as pd
import missingno as msno
import datetime
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from wordcloud import ImageColorGenerator
from pyecharts.charts import Pie
from pyecharts import options as opts
import matplotlib.pylab as plt

from module.rate import rating
from module.BubbleChart import BubbleChart
from module.ColumnNanInfo import ColumnNanInfo
from module.DeleteVal import DeleteVal
from module.WordCount import WordCount

# DataLoad 
df = pd.read_csv('./data/KoreaMovieData.csv', thousands = ',' )

# Data Cleaning 
df.columns = df.columns.str.replace('\n','')
df.set_index("순번", inplace = True)

# Filling missing value :"정보없음" 
df = df.fillna("정보없음")

# Rank Criteria Shift 
raking_df = []
for i in df["등급"]:
    raking_df.append(rating(i))
df['등급'] = raking_df

# 서울매출액 정보없음값 0으로 대체
df["서울매출액"][df["서울매출액"] == "정보없음"] = 0 
df["서울매출액"] = df["서울매출액"].astype(int)

# movie type split Indie film | film
indiefilm = df[df["영화구분"] == "독립/예술영화"]
film = df[df["영화구분"] == "일반영화"] 

# exploratory Data Analysis

## 1. count movie number by movie type

ratio = df['영화구분'].value_counts()
labels = df['영화구분'].value_counts().index
wedgeprops = {'width':0.7, 'edgecolor':'w', 'linewidth':5}
colors = ['seagreen','mediumpurple']
explode = [0, 0.10]

plt.figure(figsize=(15,8))

plt.pie(ratio, labels=labels, autopct='%.0f%%', startangle=180, counterclock=True,
       wedgeprops=wedgeprops, colors=colors, textprops={'fontsize': 20}, explode = explode)

plt.text(1.4, 1, f"독립영화 작품수 {df['영화구분'].value_counts().values[1]}", fontsize=15)
plt.text(1.4, 0.8, f"일반영화 작품수 {df['영화구분'].value_counts().values[0]}", fontsize=15)

plt.axis('equal')
plt.title('영화 구분에 따른 전체 개봉영화 작품수', fontsize=20)
plt.savefig("./image/piechart1.png")


# 월별 전체 영화 개봉 작품수 파일 
# 개봉일 정보 없는 데이터들은 drop
df_open = df[df["개봉일"] != "정보없음"]

# 개봉일에 따른 영화 갯수 파악을 위한 전처리 작업 
df_open["개봉일"] = df_open["개봉일"].str.split("-").str[0] + df_open["개봉일"].str.split("-").str[1]
df_open["개봉일"] = df_open["개봉일"].astype(int)
df_open = df_open[df_open["개봉일"] >= 201101]

# 데이트 타임으로 형 변환 후 그래프화 작업
df_open["개봉일"] = pd.to_datetime(df_open["개봉일"], format="%Y%m")
df_open1 = df_open[df_open["영화구분"] == "일반영화"]
df_open2 = df_open[df_open["영화구분"] != "일반영화"]


# 연도별 전체 영화 개봉작품 수
plt.figure(figsize=(15,8))
plt.rc('font',size=20)

plt.plot(df_open1.groupby(df_open1["개봉일"]).size(),color = 'darkkhaki', linewidth=5, linestyle=':', label='일반영화')
plt.plot(df_open2.groupby(df_open2["개봉일"]).size(),color ='teal', linewidth=5, label='독립/예술영화')

plt.legend(loc=8) 
plt.grid(True, axis='y')
plt.title("월별 전체 영화 개봉작품수", fontsize=20)
plt.xlabel('개봉일')
plt.ylabel('영화 개수')
plt.savefig("./image/plotChart1.png")
