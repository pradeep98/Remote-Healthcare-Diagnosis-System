
# coding: utf-8

# In[15]:
#import os
#os.system("cp data.csv dummy.csv")

f=open("dataLimited703.csv","r")
data=[]

for i in f:
	try:	

		data.append(list(map(float,i.split(","))))
	except:
		xx=1

#os.system("rm dummy.csv")

# In[16]:
# preproc imports
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import preprocessing as preproc
import numpy
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import random
#from imblearn.over_sampling import SMOTE
#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome
datafile="dataLimited703.data"
headers=['Pregnancies', 'Glucose', 'Insulin', 'BMI','DiabetesPedigreeFunction', 'Age', 'Outcome']
dataset=pd.read_csv(datafile, names=headers)

'''
dataset.hist()
plt.xlabel('Outcome', fontsize=10)
plt.ylabel('Outcome', fontsize=10)
plt.savefig("histograms.png")
plt.show()

scatter_matrix(dataset)
plt.xlabel('Outcome', fontsize=10)
plt.ylabel('Outcome', fontsize=10)
plt.savefig("scattePlotMatrix.png")
plt.show()
'''
len(data)

#  Undersampling

import numpy
from sklearn.utils import resample
#from imblearn.over_sampling import SMOTE

df_majority = dataset[dataset['Outcome']==0]
df_minority = dataset[dataset['Outcome']==1]

df_majority_downsampled = resample(df_majority, 
                          replace=False,    # sample without replacement
                          n_samples=df_minority['Outcome'].size,  # match minority class
                          random_state=7) # reproducible results

diabetes_mod = pd.concat([df_majority_downsampled, df_minority])

diabetes_mod=diabetes_mod.sample(frac=1).reset_index(drop=True)

#df_downsampled = diabetes_mod[(diabetes_mod.BloodPressure != 0) & (diabetes_mod.BMI != 0) & (diabetes_mod.Glucose != 0)]
df_downsampled = diabetes_mod[(diabetes_mod.BMI != 0) & (diabetes_mod.Glucose != 0)]
#corr = df_downsampled.corr()
#corr

corr = df_downsampled.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,len(df_downsampled.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(df_downsampled.columns)
ax.set_yticklabels(df_downsampled.columns)
plt.savefig("correlation_undersample.png")
#plt.show()


print("downsampled shape ",df_downsampled.shape)
#print(df_downsampled)
'''
df_downsampled.hist()
plt.savefig("histograms_undersample.png")
plt.show()

scatter_matrix(df_downsampled)
plt.savefig("scattePlotMatrix_undersample.png")
plt.show()
'''
scaler = MinMaxScaler()
#df_downsampled = scaler.fit_transform(df_downsampled)

train_target_downsampled=[]
train_data_downsampled=[]

train_split_df_downsampled=int(len(df_downsampled)*0.9)
train_downsampled=df_downsampled[:train_split_df_downsampled]
test_downsampled=df_downsampled[train_split_df_downsampled:]

#df_downsampled = pd.DataFrame(df_downsampled,index = df_downsampled.index,columns = df_downsampled.columns)
rows = df_downsampled['Outcome'].count()

train_data_downsampled = pd.DataFrame({'Pregnancies':train_downsampled['Pregnancies'].iloc[0:train_split_df_downsampled],'Glucose':train_downsampled['Glucose'].iloc[0:train_split_df_downsampled],'Insulin':train_downsampled['Insulin'].iloc[0:train_split_df_downsampled],'BMI':train_downsampled['BMI'].iloc[0:train_split_df_downsampled],'DiabetesPedigreeFunction':train_downsampled['DiabetesPedigreeFunction'].iloc[0:train_split_df_downsampled],'Age':train_downsampled['Age'].iloc[0:train_split_df_downsampled]},index=train_downsampled.index[0:train_split_df_downsampled])

train_target_downsampled = pd.DataFrame({'Outcome':train_downsampled['Outcome'].iloc[0:train_split_df_downsampled]},index = train_downsampled.index[0:train_split_df_downsampled])

test_data_downsampled = pd.DataFrame({'Pregnancies':test_downsampled['Pregnancies'].iloc[:rows+1-train_split_df_downsampled],'Glucose':test_downsampled['Glucose'].iloc[:rows+1-train_split_df_downsampled],'Insulin':test_downsampled['Insulin'].iloc[:rows+1-train_split_df_downsampled],'BMI':test_downsampled['BMI'].iloc[:rows+1-train_split_df_downsampled],'DiabetesPedigreeFunction':test_downsampled['DiabetesPedigreeFunction'].iloc[:rows+1-train_split_df_downsampled],'Age':test_downsampled['Age'].iloc[:rows+1-train_split_df_downsampled]},index=test_downsampled.index[:rows+1-train_split_df_downsampled])

test_target_downsampled = pd.DataFrame({'Outcome':test_downsampled['Outcome'].iloc[:rows+1-train_split_df_downsampled]},index = test_downsampled.index[:rows+1-train_split_df_downsampled])



#  Undersampling

max0,max1,max2,max3,max4,max5,max6,max7=0,0,0,0,0,0,0,0
min0,min1,min2,min3,min4,min5,min6,min7=1000,1000,1000,1000,1000,1000,1000,1000
for i in data:
	if(max0<i[0]):
		max0=i[0]
	if(max1<i[1]):
		max1=i[1]
	if(max2<i[2]):
		max2=i[2]
	if(max3<i[3]):
		max3=i[3]
	if(max4<i[4]):
		max4=i[4]
	if(max5<i[5]):
		max5=i[5]
		
	if(min0>i[0]):
		min0=i[0]
	if(min1>i[1]):
		min1=i[1]
	if(min2>i[2]):
		min2=i[2]
	if(min3>i[3]):
		min3=i[3]
	if(min4>i[4]):
		min4=i[4]
	if(min5>i[5]):
		min5=i[5]
	
for i in data:
	i[0]=(i[0]-min0)/(max0-min0)
	i[1]=(i[1]-min1)/(max1-min1)
	i[2]=(i[2]-min2)/(max2-min2)
	i[3]=(i[3]-min3)/(max3-min3)
	i[4]=(i[4]-min4)/(max4-min4)
	i[5]=(i[5]-min5)/(max5-min5)
# In[17]:


random.shuffle(data)
random.shuffle(data)
random.shuffle(data)
train_split=int(len(data)*0.9)
train=data[:train_split]
test=data[train_split:]



# In[18]:


train_target=[]
train_data=[]
for i in train:
    train_target.append(int(i[-1]))
    train_data.append(i[:-1])
test_target=[]
test_data=[]
for i in test:
    test_target.append(int(i[-1]))
    test_data.append(i[:-1])


# In[19]:


import keras
from keras.layers import Dense
from keras.models import Sequential


# In[20]:


model=Sequential()
model.add(Dense(12,input_dim=6,init="uniform",activation="relu"))
model.add(Dense(8,init="uniform",activation="relu"))
model.add(Dense(1,init="uniform",activation="sigmoid"))

#		undersampling

model_downsampled=Sequential()
model_downsampled.add(Dense(12,input_dim=6,init="uniform",activation="relu"))
model_downsampled.add(Dense(8,init="uniform",activation="relu"))
model_downsampled.add(Dense(1,init="uniform",activation="sigmoid"))


# In[21]:


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#	undersampling
model_downsampled.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# In[22]:


model.summary()
#  undersampling
model_downsampled.summary()
# In[23]:


train_data


# In[24]:


import numpy as np
train_data=np.array(train_data)
train_target=np.array(train_target)

#  undersampling

train_data_downsampled=np.array(train_data_downsampled)
train_target_downsampled=np.array(train_target_downsampled)

# In[25]:


# train_data_new=train_data.reshape(-1,*train_data.shape)
# train_target_new=train_target.reshape(-1,*train_target.shape)


# In[26]:


print("Normal train_data ",train_data.shape)
print("Normal train_target ",train_target.shape)


# In[27]:


history=model.fit(x=train_data,y=train_target,epochs=200,verbose=0,validation_split=0.1,shuffle=True,)

#undersampling
print("train_data_downsampled ",train_data_downsampled.shape)
print("train_target_downsampled ",train_target_downsampled.shape)

history_downsampled=model_downsampled.fit(x=train_data_downsampled,y=train_target_downsampled,epochs=200,verbose=0,validation_split=0.1,shuffle=True,)

# In[28]:


import matplotlib.pyplot as plt


# In[29]:


#print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("accuracy.png")
plt.show()


# In[30]:


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("error.png")
plt.show()

#    undersampling

plt.plot(history_downsampled.history['accuracy'])
plt.plot(history_downsampled.history['val_accuracy'])
plt.title('model downsampled accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("accuracy_downsampled.png")
plt.show()

plt.plot(history_downsampled.history['loss'])
plt.plot(history_downsampled.history['val_loss'])
plt.title('model downsampled loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("error_downsampled.png")
plt.show()


# In[31]:
#    Printing Normal input data
print("----------------------Printing Normal input data--------------------")
acc=model.evaluate(x=np.array(test_data),y=np.array(test_target),verbose=2)
print("Normal error, Normal Accuracy ",acc)

#    undersampling





# In[43]:

#3	78	50	32	88	31	0.248	26	1
#10	115	0	0	0	35.3	0.134	29	0
#2	197	70	45	543	30.5	0.158	53	1


#x=train_data[4]
#x=[2	197	70	45	543	30.5	0.158	53	1]
#x0=8	183	64	0	0	23.3	0.672	32	1
#x1=1	89	66	23	94	28.1	0.167	21	0
#x2=0	137	40	35	168	43.1	2.288	33	1
#x3=5	116	74	0	0	25.6	0.201	30	0
#x4=3	78	50	32	88	31	0.248	26	1
#x5=1	103	80	11	82	19.4	0.491	22	0
#x6=1	101	50	15	36	24.2	0.526	26	0
#x7=5	88	66	21	23	24.4	0.342	30	0


x=[2,	197,	543,	30.5	,0.158	,53]
y=1
x0=[8	,183,	0,	23.3,	0.672,	32]
y0=1
x1=[1,	89,	94,	28.1,	0.167,	21]
y1=	0
x2=[0,	137,	168,	43.1,	2.288,	33]
y2=	1
x3=[5,	116,	0,	25.6	,0.201	,30]
y3=	0
x4=[3,	78,	88,	31,	0.248,	26]
y4=	1
x5=[1,	103,	82,	19.4,	0.491,	22]
y5=	0
x6=[1,	101,	36,	24.2,	0.526,	26]
y6=	0
x7=[5,	88,	23,	24.4,	0.342,	30]
y7=	0
#x=train_data[21]
#y=train_target[21]
print(x)
a=np.array(x)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")

a=np.array(x0)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y0)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x1)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y1)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x2)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y2)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x3)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y3)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")

a=np.array(x4)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y4)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")

a=np.array(x5)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y5)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	
	
a=np.array(x6)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y6)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	
	
a=np.array(x7)
a.shape
a=a.reshape(6,)
pred=model.predict_classes(np.array([a]))
print("expected value-> ",y7)
print("calculated value-> ",pred)
if(pred):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	
	#for i in data:
	#	print(i)

# undersampling

print("----------------------Printing downsampled input data--------------------")

acc_downsampled=model_downsampled.evaluate(x=np.array(test_data_downsampled),y=np.array(test_target_downsampled),verbose=2)
print("Downsampled error and accuracy ",acc_downsampled)

x=train_data_downsampled[21]
y=train_target_downsampled[21]
print(x)
a=np.array(x)
a.shape
a=a.reshape(6,)
pred_downsampled=model_downsampled.predict_classes(np.array([a]))
print("expected value-> ",y)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x0)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y0)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x1)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y1)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x2)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y2)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")
	
a=np.array(x3)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y3)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")

a=np.array(x4)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y4)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	

a=np.array(x5)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y5)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	
	
a=np.array(x6)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y6)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	
	
a=np.array(x7)
a.shape
a=a.reshape(6,)
pred_downsampled=model.predict_classes(np.array([a]))
print("expected value-> ",y7)
print("calculated value-> ",pred_downsampled)
if(pred_downsampled):
	print("Patient has diabetes")
else:
	print("Patient doesn't have diabetes")	


