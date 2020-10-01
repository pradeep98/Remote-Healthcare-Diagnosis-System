var mainApp = {};
	
(function(){
//import app_fireBase from 'firebase.js';	

	
	window.app_firebase = firebase;
	
	
	var uid = null;
	firebase.auth().onAuthStateChanged(function(user) {
	  if (user) {
		// User is signed in.
		console.log("yaha kya hota hai!");
		uid = user.uid;
		window.globalUid = uid;
		//console.log("test "+window.globalUid);
		//setTimeout(authPromise,2000);
	  }else{
		uid = null;
		console.log("yaha kya hota hai....!");
		window.location.replace("index.html");
	  }
	});
	
	function logOut(){
		console.log("aa gaya!");
		firebase.auth().signOut();
		
	}
	
	window.mainApp.logOut = logOut;
	
	
	
})();