import warnings
warnings.filterwarnings(action='ignore')

from module.Font import Fontmanager
path = Fontmanager()

# module 
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
