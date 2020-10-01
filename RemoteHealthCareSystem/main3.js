// Your web app's Firebase configuration
var firebaseConfig = {
apiKey: "AIzaSyBOHdTKorMRZwLWqaXxnXPVFiQvIUBOXSU",
authDomain: "remotehealthcare-c1d18.firebaseapp.com",
databaseURL: "https://remotehealthcare-c1d18.firebaseio.com",
projectId: "remotehealthcare-c1d18",
storageBucket: "remotehealthcare-c1d18.appspot.com",
messagingSenderId: "295505897713",
appId: "1:295505897713:web:34fc17a8b1470cd59ae150",
measurementId: "G-GDGJN0SVYY"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();



var database = firebase.database();

auth = firebase.auth();



firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    console.log(user);
    console.log("test signed in "+firebase.auth().currentUser.uid);
  
  var data_ref = database.ref("users/"+firebase.auth().currentUser.uid+"/data_test_1");
	
	data_ref.on("value",gotVal,gotErr);
	data_ref.on("child_added", gotVal);
  
  } else {
    console.log("test not signed in "+firebase.auth().currentUser.uid);
  }
});



//firebase.auth().currentUser.uid
//"users/"+firebase.auth().currentUser.uid+"/data_test_1"
//var data_ref = database.ref("users/"+window.globalUid+"/data_test_1");


function gotVal(val, lol){
	table1=document.getElementById('heartRate');
	table2=document.getElementById('bloodPressure');
	table3=document.getElementById('bloodGlucose');
	table4=document.getElementById('heartAttack');
	personal7=document.getElementById('headName');
	
	obj=val.val();
	console.log("aakhri prahar1 "+Object.keys(obj));
	console.log("aakhri prahar2 "+Object.keys(obj)[Object.keys(obj).length-1]);
	key=Object.keys(obj)[Object.keys(obj).length-1];
	obj=obj[key];
	console.log("aakhri prahar3 "+obj[key]);
	var imag=["like.png","newBP1.png","heartrate.png","bloodglucose.png"];
	
	keys=Object.keys(obj);

	row1="";
	row2="";
	row3="";
	row4="";
	row07="";
	
	row1+=`${obj['heart_rate']} `;
	row2+=`${obj['sbp']} / ${obj['dbp']}`;
	row3+=` ${obj['glucose_level']} `;
	row4+=`${obj['heart_attack']} `;
	row07+=`${obj['fname']} ${obj['lname']}`;
	/*for(i=0;i<keys.length;i++){

		console.log(keys[i]);
		console.log(obj[keys[i]]);
		// obj["heatbeat"]
		rows+=`<tr> <th>${keys[i]}</th> <td> <div ><img src=${imag[2]}></div> <div> ${obj[keys[i]]}  </div></td> </tr>`;
		// rows+=`lol`;
		console.log(rows);
	}*/
	table1.innerHTML=row1;
	table2.innerHTML=row2;
	table3.innerHTML=row3;
	table4.innerHTML=row4;
	personal7.innerHTML=row07;
	
	
	table11=document.getElementById('heartRate1');
	table12=document.getElementById('bloodPressure1');
	table13=document.getElementById('bloodGlucose1');
	table14=document.getElementById('heartAttack1');

	row11="";
	row12="";
	row13="";
	row14="";
	
	row11+=`<h2 style=" color:#3face4;"> ${obj['heart_rate']} </h2>`;
	row12+=`<h2 style=" color:#3face4;"> ${obj['sbp']} / ${obj['dbp']} </h2>`;
	row13+=`<h2 style=" color:#3face4;"> ${obj['glucose_level']} </h2>`;
	row14+=`<h2 style=" color:#3face4;"> ${obj['heart_attack']} </h2>`;
	/*for(i=0;i<keys.length;i++){

		console.log(keys[i]);
		console.log(obj[keys[i]]);
		// obj["heatbeat"]
		rows+=`<tr> <th>${keys[i]}</th> <td> <div ><img src=${imag[2]}></div> <div> ${obj[keys[i]]}  </div></td> </tr>`;
		// rows+=`lol`;
		console.log(rows);
	}*/
	table11.innerHTML=row11;
	table12.innerHTML=row12;
	table13.innerHTML=row13;
	table14.innerHTML=row14;
	
	
	
}


function gotErr(val){
    console.log("Error...");
    console.log(val);
}

//data_ref.orderByChild("time").on("child_added", function(snapshot) {
//  console.log(">>");
//  console.log(snapshot.val());
//});


//data_ref.on("value",gotVal,gotErr);
//data_ref.on("child_added", gotVal);
