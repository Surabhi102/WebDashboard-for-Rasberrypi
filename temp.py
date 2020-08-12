from flask import Flask,render_template, request, send_file
import RPi.GPIO as GPIO
import pandas as pd
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
plt.style.use('ggplot')


fig, ax = plt.subplots()
df = pd.ExcelFile('book1.xlsx')
df_read = pd.read_excel(df,'Sheet1')
time = df_read['data']
temp = df_read['temp']
plt.plot(time,temp,color='blue')
plt.xlabel('degree')
plt.ylabel('time')
plt.title('time series of temperature')
canvas = FigureCanvas(fig)
img = BytesIO()
fig.savefig("mathplot.png")
img.seek(0)

