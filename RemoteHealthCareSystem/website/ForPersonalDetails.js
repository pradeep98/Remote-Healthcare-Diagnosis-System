// Your web app's Firebase configuration

firebase.analytics();


var database = firebase.database();


firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    console.log(user);
    console.log("test signed in "+firebase.auth().currentUser.uid);
  
  var data_ref = database.ref("users/"+firebase.auth().currentUser.uid+"/data_test_1");
  data_ref.on("value",gotVal,gotErr);
  
  } else {
    console.log("test not signed in "+firebase.auth().currentUser.uid);
  }
});

console.log("test not ");
console.log("test "+database.ref("users/"+"XMWul54ZqfUhlTIIaZqV7CjKlHr2"+"/data_test_1"));
//var data_ref = database.ref("users/"+firebase.auth().currentUser.uid+"/data_test_1");





function gotVal(val){

	obj=val.val();
	console.log("aakhri prahar1 "+Object.keys(obj));
	console.log("aakhri prahar2 "+Object.keys(obj)[Object.keys(obj).length-1]);
	key=Object.keys(obj)[Object.keys(obj).length-1];
	obj=obj[key];
	console.log("aakhri prahar3 "+obj[key]);
	var imag=["like.png","newBP1.png","heartrate.png","bloodglucose.png"];
	keys=Object.keys(obj);

	
	personal1=document.getElementById('naam');
	personal2=document.getElementById('email');
	personal3=document.getElementById('phone');
	personal4=document.getElementById('age');
	personal5=document.getElementById('bmi');
	personal6=document.getElementById('date');
	personal7=document.getElementById('headName');
	
	
	row01="";
	row02="";
	row03="";
	row04="";
	row05="";
	row06="";
	row07="";
	
	row01+=`<h2 style=" color:#3face4;"> ${obj['fname']} ${obj['lname']} </h2>`;
	row02+=`<h2 style=" color:#3face4;"> ${obj['email']}</h2>`;
	row03+=`<h2 style=" color:#3face4;"> ${obj['phone']} </h2>`;
	row04+=`<h2 style=" color:#3face4;"> ${obj['age']} </h2>`;
	row05+=`<h2 style=" color:#3face4;"> ${obj['bmi']} </h2>`;
	
	var d = new Date(obj['Time']*1000);
	
	row06+=`<h2 style=" color:#3face4;"> ${d} </h2>`;
	row07+=`${obj['fname']} ${obj['lname']}`;
	
	
	personal1.innerHTML=row01;
	personal2.innerHTML=row02;
	personal3.innerHTML=row03;
	personal4.innerHTML=row04;
	personal5.innerHTML=row05;
	personal6.innerHTML=row06;
	personal7.innerHTML=row07;
	
	
	persona21=document.getElementById('naam1');
	persona22=document.getElementById('email1');
	persona23=document.getElementById('phone1');
	persona24=document.getElementById('age1');
	persona25=document.getElementById('bmi1');
	persona26=document.getElementById('date1');

	row11="";
	row12="";
	row13="";
	row14="";
	row15="";
	row16="";
	
	row11+=`<h2 style=" color:#3face4;"> ${obj['fname']} ${obj['lname']}  </h2>`;
	row12+=`<h2 style=" color:#3face4;"> ${obj['email']} / ${obj['dbp']} </h2>`;
	row13+=`<h2 style=" color:#3face4;"> ${obj['phone']} </h2>`;
	row14+=`<h2 style=" color:#3face4;"> ${obj['age']} </h2>`;
	row15+=`<h2 style=" color:#3face4;"> ${obj['bmi']} </h2>`;
	
	d = new Date(obj['Time']*1000);
	
	row16+=`<h2 style=" color:#3face4;"> ${d} </h2>`;
	/*for(i=0;i<keys.length;i++){

		console.log(keys[i]);
		console.log(obj[keys[i]]);
		// obj["heatbeat"]
		rows+=`<tr> <th>${keys[i]}</th> <td> <div ><img src=${imag[2]}></div> <div> ${obj[keys[i]]}  </div></td> </tr>`;
		// rows+=`lol`;
		console.log(rows);
	}*/
	persona21.innerHTML=row01;
	persona22.innerHTML=row02;
	persona23.innerHTML=row03;
	persona24.innerHTML=row04;
	persona25.innerHTML=row05;
	persona26.innerHTML=row06;
	
}


function gotErr(val){
    console.log("Error...");
    console.log(val);
}

//data_ref.on("value",gotVal,gotErr);

