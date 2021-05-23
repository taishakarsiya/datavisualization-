import pandas as pd 
import plotly.express as px
import random
import csv 
import statistics

df = pd.read_csv("finding-correlation-master")
fig = px.bar(df, x="marks in percentage", y="days present", color="roll number", title='marks in percent vs days present ')
fig.show()