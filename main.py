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

# Filling missing value :0 
df = df.fillna("정보없음")

# Rank Criteria Shift 
raking_df = []
for i in df["등급"]:
    raking_df.append(rating(i))
df['등급'] = raking_df

# movie type split Indie film | film
indiefilm = df[df["영화구분"] == "독립/예술영화"]
film = df[df["영화구분"] == "일반영화"] 
