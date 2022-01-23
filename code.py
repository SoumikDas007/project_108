import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")
graph = ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist=True)

graph.show()