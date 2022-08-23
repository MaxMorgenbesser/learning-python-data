import data
grades = data.grades
import matplotlib.pyplot as plt
import numpy as np

math = []
science = []
english = []
compSci=[]

for i in grades.values():
   math.append(i["math"])
   science.append(i["science"])
   english.append(i["english"])
   compSci.append(i["computer science"])

x=np.array(science)
y=np.array(compSci)

a, b = np.polyfit(x, y, 1)

plt.scatter(x, y)
plt.plot(x, a*x+b, color='blue')
plt.show()





