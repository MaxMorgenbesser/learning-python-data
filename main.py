# import data
# grades = data.grades
# import matplotlib.pyplot as plt
# import numpy as np
#
# math = []
# science = []
# english = []
# compSci=[]
#
# for i in grades.values():
#    math.append(i["math"])
#    science.append(i["science"])
#    english.append(i["english"])
#    compSci.append(i["computer science"])
#
# x=np.array(science)
# y=np.array(compSci)
#
# a, b = np.polyfit(x, y, 1)
#
# plt.scatter(x, y)
# plt.plot(x, a*x+b, color='blue')
# plt.show()
#

import numpy as np
import matplotlib.pyplot as plt

from pandas import read_csv
import csv
data = read_csv('student-mat.csv')

absences = data['absences'].tolist()
studyTime = data['studytime'].tolist()

y=np.array(absences)
x=np.array(studyTime)
a, b = np.polyfit(x, y, 1)
plt.scatter(x, y)
plt.plot(x, a*x+b, color='blue')
plt.show()


