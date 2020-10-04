#from sklearn.cross_validation import cross_val_score
#from functools import reduce
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Flatten
from keras.layers.core import Activation
from keras.layers import LeakyReLU
#from keras.optimizers import SGD
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings("ignore")
#from GSS.iiGSS import GSS
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

from keras.models import model_from_json
import pandas as pd
import math
###     diastolic systolic

import temp3

# coding: utf-8

# In[7]:


data=[]
data = pd.read_csv("fram.csv",delimiter=",")
data = data.dropna()
scaler = MinMaxScaler()
data_nm = scaler.fit_transform(data)

#len(data)


import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import preprocessing as preproc
import numpy
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import random
import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" 
datafile="fram.data"
headers=['age','sysBP','diaBP','BMI','heartRate','glucose','TenYearCHD']
dataset=pd.read_csv(datafile, names=headers)

#len(data)
# male	age	education	currentSmoker	cigsPerDay	BPMeds	prevalentStroke	prevalentHyp	diabetes	totChol	sysBP	diaBP	BMI	heartRate	glucose	TenYearCHD

import numpy
from sklearn.utils import resample
#from imblearn.over_sampling import SMOTE

df_majority = dataset[dataset['TenYearCHD']==0]
df_minority = dataset[dataset['TenYearCHD']==1]

df_majority_downsampled = resample(df_majority, 
                          replace=False,    # sample without replacement
                          n_samples=df_minority['TenYearCHD'].size,  # match minority class
                          random_state=6) # reproducible results

diabetes_mod = pd.concat([df_majority_downsampled, df_minority])

diabetes_mod=diabetes_mod.sample(frac=1).reset_index(drop=True)

#df_downsampled = diabetes_mod[(diabetes_mod.BloodPressure != 0) & (diabetes_mod.BMI != 0) & (diabetes_mod.Glucose != 0)]
#df_downsampled = diabetes_mod[(diabetes_mod.age != 0) & (diabetes_mod.diabetes != 0) & (diabetes_mod.totChol != 0) &
#(diabetes_mod.sysBP != 0) & (diabetes_mod.diaBP != 0) & (diabetes_mod.BMI != 0) & (diabetes_mod.heartRate != 0) & (diabetes_mod.glucose != 0)]
#corr = df_downsampled.corr()
df_downsampled = diabetes_mod
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
plt.savefig("correlation_undersample522019.png")
#plt.show()

# In[17]:


import random
import random
random.shuffle(data_nm)
random.shuffle(data_nm)
random.shuffle(data_nm)
data_nm = pd.DataFrame(data_nm,index = data.index,columns = data.columns)
rows = data['TenYearCHD'].count()
train_size = int(math.ceil(rows*0.8))
train_size = int(train_size)



# In[18]:




# In[16]:male	age	education	currentSmoker	cigsPerDay	BPMeds	prevalentStroke	prevalentHyp	diabetes	totChol	sysBP	diaBP	BMI	heartRate	glucose	TenYearCHD


train_data = pd.DataFrame({'age':data_nm['age'].iloc[0:train_size],'sysBP':data_nm['sysBP'].iloc[0:train_size],'diaBP':data_nm['diaBP'].iloc[0:train_size],'BMI':data_nm['BMI'].iloc[0:train_size],'heartRate':data_nm['heartRate'].iloc[0:train_size],'glucose':data_nm['glucose'].iloc[0:train_size]},index=data_nm.index[0:train_size])

train_target = pd.DataFrame({'TenYearCHD':data_nm['TenYearCHD'].iloc[0:train_size]},index = data_nm.index[0:train_size])

test_data = pd.DataFrame({'age':data_nm['age'].iloc[train_size:rows+1],'sysBP':data_nm['sysBP'].iloc[train_size:rows+1],'diaBP':data_nm['diaBP'].iloc[train_size:rows+1],'BMI':data_nm['BMI'].iloc[train_size:rows+1],'heartRate':data_nm['heartRate'].iloc[train_size:rows+1],'glucose':data_nm['glucose'].iloc[train_size:rows+1]},index=data_nm.index[train_size:rows+1])

test_target = pd.DataFrame({'TenYearCHD':data_nm['TenYearCHD'].iloc[train_size:rows+1]},index=data_nm.index[train_size:rows+1])

scaler_for_predictions = MinMaxScaler()
scaler_for_predictions.fit(data['TenYearCHD'].values.reshape(-1,1))


# In[19]:


import keras
from keras.layers import Dense
from keras.models import Sequential


# In[20]:
from keras import regularizers

model=Sequential()
model.add(Dense(128,input_dim=6,init="glorot_uniform",activation="tanh",kernel_regularizer=regularizers.l2(0.01),activity_regularizer=regularizers.l1(0.01)))
model.add(Dropout(0.5))
model.add(Dense(100,init="glorot_uniform",activation="tanh",kernel_regularizer=regularizers.l2(0.01),activity_regularizer=regularizers.l1(0.01)))
model.add(Dropout(0.3))
model.add(Dense(64,init="glorot_uniform",activation="tanh",kernel_regularizer=regularizers.l2(0.01),activity_regularizer=regularizers.l1(0.01)))
model.add(Dropout(0.6))
model.add(Dense(1,init="uniform",activation="sigmoid"))


# In[21]:


model.compile(loss='binary_crossentropy', optimizer=keras.optimizers.adam(lr=0.0001), metrics=['accuracy'])


# In[22]:


#model.summary()


# In[23]:


#train_data


# In[24]:


import numpy as np
train_data=np.array(train_data)
train_target=np.array(train_target)


# In[25]:


# train_data_new=train_data.reshape(-1,*train_data.shape)
# train_target_new=train_target.reshape(-1,*train_target.shape)


# In[26]:

# madadgar
#print(train_data.shape)
#print(train_target.shape)


# In[27]:


history=model.fit(x=train_data,y=train_target,epochs=50,verbose=0,validation_split=0.2,shuffle=True,)

# In[28]:


import matplotlib.pyplot as plt


# In[29]:
#   training

#print(history.history.keys())
# summarize history for accuracy
'''
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("accuracy5220191.png")
plt.show()


# In[30]:


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("error5220191.png")
plt.show()
'''

# In[31]:


acc_downsampled=model.evaluate(x=np.array(test_data),y=np.array(test_target),verbose=0)

print("Downsampled error and accuracy ",acc_downsampled)
# In[43]:

x = pd.DataFrame({'age':temp3.age,'sysBP':temp3.sysBp,'diaBP':temp3.diaBP,'BMI':temp3.bmi,'heartRate':temp3.hr,'glucose':temp3.gl},index=[0])
#x=[1,	39,	4,	0,	0,	0,	0,	0,	0,	195,	106,	70,	26.97,	80,	77]0
#0	61	3	1	30	0	0	1	0	225	70	95	28.58	65	103	1
#0	46	3	1	23	0	0	0	0	285	130	84	23.1	85	85	0
#0	43	2	0	0	0	0	1	0	228	180	110	30.3	77	99	0
#0	63	1	0	0	0	0	0	0	205	138	71	33.11	60	85	1



y=train_target[1]
#print(x,y)


# In[44]:


a=np.array(x)
#a.shape


# In[45]:


a=a.reshape(6,)


# In[49]:


pred=model.predict_classes(np.array([a]))


# In[50]

print("\n>>")
print(pred)
print("\n>>")
predicted=""
if(pred[0][0]==0):
	print('No Cardiac Risk!')
	predicted = "No Cardiac Risk!"
else:
	print('Possible Cardiac Risk!')
	predicted = "Possible Cardiac Risk!"


