from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
from numpy import genfromtxt, array
import math
import pandas
import numpy
import temp1
import matplotlib.pyplot as plt
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

points = genfromtxt("sys.csv", delimiter="	")
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
    
SBP_Param = {'age': x1,
				'BMI':x2,
				'hR':x3,
				'gl':x4,
                'sBP': y
               }

df = DataFrame(SBP_Param,columns=['age','BMI','hR','gl','sBP'])


X = df[['age','BMI','hR','gl']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['sBP']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)
age = temp1.age
bmi=  temp1.bmi
hr=	temp1.hr
gl=temp1.gl
email=temp1.email
fname=temp1.fname
lname=temp1.lname
phone=temp1.phone
sysBp = regr.predict([[age,bmi,hr,gl]])
#sysBp=round(sysBp[0],2)
print ('Predicted sBP: ', sysBp[0])
diaBP = temp1.diaBp
#print ('Predicted dBP: \n', diaBP)
y1=MeasuredBP(regr.coef_,regr.intercept_,x1,x2,x3,x4)
f= open("Sysnew.csv","w+")
for i in range(len(y1)):
     f.write(str(x1[i])+"	"+str(x2[i])+"	"+str(x3[i])+"	"+str(x4[i])+"	"+str(y[i])+"	"+str(y1[i])+"	"+str(y1[i]-y[i]))
     f.write("\n")
stand_dev=math.sqrt(mse(y,y1))
print('Standard Error(sBP) : ',stand_dev)
print('\n')
url = "SYSBP.data"
names = ['age','BMI','hR','gl','sBP']
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