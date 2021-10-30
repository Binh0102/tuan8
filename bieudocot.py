import matplotlib.pyplot as plt
import numpy as np

divisions=["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_averagr_marks=[70,82,73,65,68]

plt.bar(divisions,divisions_averagr_marks,color='blue')
plt.title("Bar Graph")
plt.xlabel("divisions")
plt.ylabel("Marks")
plt.show()