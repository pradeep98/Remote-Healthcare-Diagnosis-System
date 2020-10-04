// Authenticate with the first user then save the currentUser to a local variable
var previousUser = firebase.auth().currentUser;

// Authenticate with a second method and get a credential
// This example shows an email/password credential, but you can get credentials from any auth provider
// Note that using an OAuth provider as your se
var credential = firebase.auth.EmailPasswordAuthProvider.credential(email, password);
previousUser.link(credential)
 .catch(function (error) {
   // Linking will often fail if the account has already been linked. Handle these cases manually.
 });

// OAuth providers authenticate in an asynchronous manner, so you’ll want to perform the link account link in the callback.
var previousUser = firebase.auth().currentUser;
firebase.auth().signInWithPopup(new firebase.authGoogleAuthProvider())
 .then(function (result) {
 return previousUser.link(result.credential);
 })
 .catch(function (err) {
   // Handle error
 });