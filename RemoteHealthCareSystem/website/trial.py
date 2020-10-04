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
def MeasuredBP(coef,inter,x1):
	y=[]
	for i in range(len(x1)):
		y.append(coef[0]*x1[i]+inter)
	return y
def mse(a, b):
	error = 0.0
	for i in range(len(a)):
		error += (b[i] - a[i]) ** 2
	return error / len(a)
points = genfromtxt("trial.csv", delimiter=",")
#print(points)
x1=[]

y=[]
for i in range(0, len(points)):
	x1.append(points[i,1])
	y.append(points[i,0])
print(x1)
print(y)

#x1 = map(float,x1)
#y = map(float,y)
    
DBP_Param = {'ace': x1,
                'bg': y
               }

df = DataFrame(DBP_Param,columns=['ace','bg'])

min_=min(y)
max_=max(y)
X = df[['ace']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['bg']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)
ace=1.3
ans = regr.predict([[ace]])
print ('Predicted dBP: \n', ans)
y1=MeasuredBP(regr.coef_,regr.intercept_,x1)
print(regr.coef_)
print(regr.intercept_)

stand_dev=math.sqrt(mse(y,y1))
print(stand_dev)




# plot correlation matrix


