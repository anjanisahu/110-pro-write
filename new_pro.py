import csv
import plotly. express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go
new_file=pd.read_csv("Size of TV,_Average time spent watching TV in a week (hours).csv")
#list means array
#tolist se data array mein convert ho jata h
df=new_file["Size of TV"].tolist()

#mean
mean=statistics.mean(df)
print("Mean:")
print(mean)

#median
median=statistics.median(df)
print("Median:")
print(median)

#mode
mode=statistics.mode(df)
print("mode:")
print(mode)

#standard deviation
standard_deviation=statistics.stdev(df)
print("Standard Deviation:")
print(standard_deviation)

#now for bell curve
fig=ff.create_distplot([df],["result"],show_hist=False)
fig.show()



