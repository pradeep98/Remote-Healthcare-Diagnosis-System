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

var database = firebase.database()
var data_ref = database.ref("data_test_1");


function gotVal(val){
	table=document.getElementById('data');
	obj=val.val()

	key=Object.keys(obj)[0]
	obj=obj[key];
	
	var imag=["like.png","newBP1.png","heartrate.png","bloodglucose.png"]
	
	keys=Object.keys(obj);

	rows="";
	
	rows+=`<tr>`;
	rows+=`<td> <div style=""><img src=${imag[2]}></div> <div> ${obj['heart_rate']}  </div></td>`;
	rows+=`<td> <div ><img src=${imag[1]}></div> <div> ${obj['sbp']} / ${obj['dbp']} </div></td>`;
	rows+=`<td> <div ><img src=${imag[3]}></div> <div> ${obj['glucose_level']}  </div></td> `;
	rows+=`<td> <div ><img src=${imag[0]}></div> <div> ${obj['heart_attack']}  </div></td>`;
	rows+=`</tr>`;
	/*for(i=0;i<keys.length;i++){

		console.log(keys[i]);
		console.log(obj[keys[i]]);
		// obj["heatbeat"]
		rows+=`<tr> <th>${keys[i]}</th> <td> <div ><img src=${imag[2]}></div> <div> ${obj[keys[i]]}  </div></td> </tr>`;
		// rows+=`lol`;
		console.log(rows);
	}*/
	table.innerHTML=rows;
}


function gotErr(val){
    console.log("Error...");
    console.log(val);
}

data_ref.on("value",gotVal,gotErr);

