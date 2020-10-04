from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt
import pandas
import numpy
from numpy import genfromtxt, array
import math
from sklearn.metrics import mean_squared_error

def MeasuredBP(coef,inter,x1,x2,x3,x4):
	y=[]
	for i in range(len(x1)):
		y.append(coef[0]*x1[i]+coef[1]*x2[i]+coef[2]*x3[i]+coef[3]*x4[i]+inter)
	return y
def mse(a, b):
	error = 0.0
	for i in range(len(a)):
		error += (b[i] - a[i]) ** 2
	return error / len(a)
points = genfromtxt("dias.csv", delimiter="	")
#print(points)
x1=[]
x2=[]
x3=[]
x4=[]
y=[]
for i in range(0, len(points)):
	x1.append(points[i,0])
	x2.append(points[i,1])
	x3.append(points[i,2])
	x4.append(points[i,3])
	y.append(points[i,4])
    
DBP_Param = {'age': x1,
				'BMI':x2,
				'hR':x3,
				'gl':x4,
                'dBP': y
               }

df = DataFrame(DBP_Param,columns=['age','BMI','hR','gl','dBP'])

min_=min(y)
max_=max(y)
X = df[['age','BMI','hR','gl']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['dBP']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)

fname = input("Enter your First Name : ")
lname = input("Enter your Last Name : ")

age = int(input("Enter your age : "))
bmi=  float(input("Enter your bmi : "))

phone = int(input("Enter your phone number : "))
email = input("Enter your email : ")


print("Getting Heart Rate....")
import getHeartRateData
hr=	getHeartRateData.get_heartrate()
print('Heart Rate : ',hr)
print('\n')
import time
print("Blow Air now")
time.sleep(5)
#import getArduinoData
print("getting glucose level...")
import kalman2
#gl=getArduinoData.get_glucose()
gl=kalman2.kalman
print('Acetone Level : ',gl)
#gl=gl*91.38+6.3743
gl=gl*88.83358634+11.746736101317197
print('Glucose Level : ',gl)
print('\n')
diaBp = regr.predict([[age,bmi,hr,gl]])
print ('Predicted dBP: ', diaBp[0])
y1=MeasuredBP(regr.coef_,regr.intercept_,x1,x2,x3,x4)
f= open("Diasnew.csv","w+")
err=[]
for i in range(len(y1)):
	err.append(y1[i]-y[i])
	f.write(str(x1[i])+"	"+str(x2[i])+"	"+str(x3[i])+"	"+str(x4[i])+"	"+str(y[i])+"	"+str(y1[i])+"	"+str(y1[i]-y[i]))
	f.write("\n")
#err=[x*x for x in err]
stand_dev=math.sqrt(mse(y,y1))
print('Standard Error(dBP) : ' ,stand_dev)
print('\n')
url = "DIASBP.data"
names = ['age','BMI','hR','gl','dBP']
data = pandas.read_csv(url, names=names)
correlations = data.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,5,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
#plt.show()


