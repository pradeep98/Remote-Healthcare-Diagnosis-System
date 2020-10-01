// Initialize Firebase
(function(){
	var config = {
		apiKey: "AIzaSyBOHdTKorMRZwLWqaXxnXPVFiQvIUBOXSU",
		authDomain: "remotehealthcare-c1d18.firebaseapp.com",
		databaseURL: "https://remotehealthcare-c1d18.firebaseio.com",
		projectId: "remotehealthcare-c1d18",
		storageBucket: "remotehealthcare-c1d18.appspot.com",
		messagingSenderId: "295505897713",
		appId: "1:295505897713:web:34fc17a8b1470cd59ae150",
		measurementId: "G-GDGJN0SVYY"
	};
	firebase.initializeApp(config);
	
	
	
	/*
	const txtEmail = document.getElementById('txtEmail');
	const txtPassword = document.getElementById('txtEmail');
	const btnLogin = document.getElementById('btnLogin');
	const btnSignup = document.getElementById('btnSignup');
	const btnLogout = document.getElementById('btnLogout');

		//   add login event
		btnLogin.addEventListener('click', e => {
			const email = txtEmail.value;
			const pass = txtPassword.value;
			const auth = firebase.auth();
			// sign in
			const promise = auth.signInWithEmailAndPassword(email,pass);
			promise.catch(e => console.log(e.message));


		});
		
		/// create user
		btnSignup.addEventListener('click', e => {
			const email = txtEmail.value;
			const pass = txtPassword.value;
			const auth = firebase.auth();
			// sign in
			const promise = auth.createUserWithEmailAndPassword(email,pass);
			promise.catch(e => console.log(e.message));


		});
		
		//    add a realtime listner
		firebase.auth().onAuthStateChanged(firebaseUser => {
			if(firebaseUser){
				console.log(firebaseUser);
				
			}else{
				console.log('not logged in');
			}
		
		});
		*/
}());