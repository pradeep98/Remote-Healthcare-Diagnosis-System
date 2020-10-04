# Remote-Healthcare-Diagnosis-System
### Objective:
  <ul>
  <li>Detection of patient’s vital life signs using sensors.</li>
  <li><ul>This includes Measuring:
    <li>blood glucose level,</li>
    <li>systolic blood pressure,</li>
    <li>diastolic blood pressure and</li>
    <li>possible heart attack</li>
  by using non-invasive methods.</ul> </li>
  <li>Sending data to cloud storage</li>
  <li>Providing the detected data for remote viewing</li></ul>

### Blood Glucose Monitoring:
   <ul><li>Conventional way of detecting glucose levels involves pricking the finger and collecting blood sample.</li>
    <li><b>Acetone Level:</b> Calculated using TGS-822 sensor.</li>
    <li><b> Why Acetone? </b> A diabetic patient's pancreas do not make enough insulin for the breakdown of sugar/glucose.</li>
  &emsp;&emsp; At such times, cells do not get enough energy and body starts burning fat which also creates acetone.
     <li>The calculated acetone level is mapped with blood glucose level using Linear Regression. </li></ul>
     &emsp;&emsp; Liner Regression Error: 18.09
    
### Blood Pressure Monitoring:
 <ul>
  <li>Blood pressure depends on various factors like glucose level, heart rate, BMI, age. </li>
   <li>All these factors are used to estimate the systolic and diastolic blood pressure using Linear Regression.</li></ul>
    <ul> Liner Regression Error:
       <li> Diastolic BP: 10.75</li>
       <li> Systolic BP: 18.99</li></ul>
   
   ![Diastolic BP correlation matrix](https://github.com/pradeep98/Remote-Healthcare-Diagnosis-System/blob/master/RemoteHealthCareSystem/aa.png?raw=true)
   
   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Diastolic BP correlation matrix
   
   ![Systolic BP correlation matrix](https://github.com/pradeep98/Remote-Healthcare-Diagnosis-System/blob/master/RemoteHealthCareSystem/aa.png?raw=true)
  
   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  Systolic BP correlation matrix
    
### Cardiac Arrest Prediction:
 <ul> <li>Predicted cardiac risk based on age, BMI, heart rate, systolic BP, diastolic BP, blood glucose level.</li>
  <li>Binary classification using ANN.</li></ul>
  &emsp;&emsp; Classification Accuracy: 85.52 %
  
  ![Heart Attack correlation matrix](https://github.com/pradeep98/Remote-Healthcare-Diagnosis-System/blob/master/RemoteHealthCareSystem/correlation_undersample522019.png?raw=true)
  
   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  Cardiac Risk Correlation Matrix
  

### Dataset: [Kaggle Pima Indian Diabetes](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

### Detailed Report: [Here](https://drive.google.com/file/d/1MEQ8P5gyD_rvF-z__nmokqsjowU-KQM2/view?usp=sharing)

