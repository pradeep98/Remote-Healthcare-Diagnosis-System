

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

	const txtEmail = document.getElementById('txtEmail');
	const txtPassword = document.getElementById('txtPassword');
	const btnLogin = document.getElementById('btnLogin');
	const btnSignup = document.getElementById('btnSignup');
	const btnLogout = document.getElementById('btnLogout');
	const current = document.getElementById('current');
	const personal = document.getElementById('personal');
	const records = document.getElementById('records');
	const btnLogout1 = document.getElementById('btnLogout1');
	
		//   add login event
		btnLogin.addEventListener('click', e => {
			const email = txtEmail.value;
			const pass = txtPassword.value;
			const auth = firebase.auth();
			// sign in
			const promise = auth.signInWithEmailAndPassword(email,pass);
			
			console.log('logged in');
			return window.location.href='personaldetails.html';
			promise.catch(e => console.log(e.message));
			
			
			//setTimeout(authPromise,2000)

		});
		
		/// create user
		btnSignup.addEventListener('click', e => {
			
			
			
			
			btnSignup.addEventListener('click', e => {
			const email = txtEmail.value;
			const pass = txtPassword.value;
			const auth = firebase.auth();
			// sign in
			const promise = auth.createUserWithEmailAndPassword(email,pass);
			//console.log(promise);
			console.log('signed uped');
			promise.catch(e => console.log(e.message));	
//return window.location.href='personaldetails.html';			
			//console.log(promise);
			//console.log(firebase.auth());
			//firebase.database().ref('users/' + firebase.auth()).set({email: email});
		
		});
			
		
		});
		
		/// Sign out
		
		btnLogout.addEventListener('click', e => {
			firebase.auth().signOut();
		

		});
		btnLogout1.addEventListener('click', e => {
			firebase.auth().signOut();
		

		});
		
		//    add a realtime listner
		firebase.auth().onAuthStateChanged(firebaseUser => {
			if(firebaseUser){
				console.log(firebaseUser.uid);
				return window.location.href = 'personaldetails.html';
				//usersRef.once('value', function(snapshot) {
				//if (snapshot.hasChild(theDataToAdd)) {
				//	alert('exists');
				//  }
				//});
				
				var ref = firebase.database().ref("users/");
				ref.once("value").then(function(snapshot) {
					if(snapshot.hasChild(firebaseUser.uid)){
						window.alert("lol");
						window.globalUid = firebase.auth().currentUser.uid;
					}					// true
					else{
						x=firebaseUser.uid.toString();
						
						firebase.database().ref('users/' + firebaseUser.uid).set({
							email: txtEmail.value
						});
						
						window.globalUid = firebase.auth().currentUser.uid;
						
						window.alert("not created yet");
						//firebase.database().ref('users/' + firebase.auth()).set({email: email});
						//firebase.database().ref('users/' + firebase.auth().currentUser.uid).set({email: txtEmail});
					}
				});
				
				btnLogout.classList.remove('hide');
				personal.classList.remove('hide');
				btnLogin.classList.add('hide');
				btnSignup.classList.add('hide');
				current.classList.remove('hide');
				records.classList.remove('hide');
				btnLogout1.classList.remove('hide');
				
				//return window.location.href='personaldetails.html';
				
				
			}else{
				
				
				console.log('logged out');
				btnLogout.classList.add('hide');
				btnLogin.classList.remove('hide');
				btnSignup.classList.remove('hide');
				personal.classList.add('hide');
				current.classList.add('hide');
				records.classList.add('hide');
				btnLogout1.classList.add('hide');
				
				
			}
		
		});
		
}());