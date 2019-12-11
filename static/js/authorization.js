let web_AUTH = {'title': 'WEB_AUTH'};

window.addEventListener('load', function() {

  var idToken;
  var accessToken;
  var expiresAt;

  var webAuth = new auth0.WebAuth({
    domain: 'wig.auth0.com',
    clientID: 'zOJNQh0UfldRKeHBaTSNgdPfLT5C9AgJ',
    responseType: 'token id_token',
    scope: 'openid',
    // redirectUri: window.location.href
    redirectUri: 'https://kambo.pythonanywhere.com/auth0/'

  });

  web_AUTH.webAuth = webAuth ;

  var loginBtn = document.getElementById('btn-login');
  var display_credentials = document.getElementById('display_credentials');


  var apiBtn = document.getElementById('btnId');
  apiBtn.addEventListener('click', ()=> {console.log('api request > ')} );

  loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
    webAuth.authorize();
  });

  var loginStatus = document.querySelector('.container h4');
  var loginView = document.getElementById('login-view');
//   var homeView = document.getElementById('home-view');

  // buttons and event listeners
  var homeViewBtn = document.getElementById('btn-home-view');
  var loginBtn = document.getElementById('btn-login');
  var logoutBtn = document.getElementById('btn-logout');

  const queryAPI = () => {
      console.log('queryAPI');
  }

  homeViewBtn.addEventListener('click', function() {
    // homeView.style.display = 'inline-block';
    loginView.style.display = 'none';
  });

  logoutBtn.addEventListener('click', logout);

  function handleAuthentication() {
  	console.log('handleAuthentication() ')

    webAuth.parseHash(function(err, authResult) {
      if (authResult && authResult.accessToken && authResult.idToken) {
        window.location.hash = '';
        localLogin(authResult);
        loginBtn.style.display = 'none';
        // homeView.style.display = 'inline-block';
      } else if (err) {
        // homeView.style.display = 'inline-block';
        console.log(err);
        alert(
          'Error: ' + err.error + '. Check the console for further details.'
        );
      }
      displayButtons();
    });
  }

  function localLogin(authResult) {
    // Set isLoggedIn flag in localStorage
    localStorage.setItem('isLoggedIn', 'true');


    const lstorage = localStorage.valueOf('isLoggedIn');
    console.log('localLogin() ', lstorage)

    // Set the time that the Access Token will expire at
    expiresAt = JSON.stringify(
      authResult.expiresIn * 1000 + new Date().getTime()
    );
    accessToken = authResult.accessToken;
    idToken = authResult.idToken;

    // let cad = ` *** idToken ${idToken} ****   accessToken ${accessToken} ****  expiresAt ${expiresAt}`;
    localStorage.setItem('accessToken', accessToken);
    localStorage.setItem('idToken', idToken);

    console.log('localLogin 90accessToken: ', accessToken)
    console.log('localLogin 90 idToken: ', idToken)
    console.log('expiresAt', expiresAt, new Date(parseInt(expiresAt)), "Now -> ", new Date() )

    display_credentials.innerText += 'localStorage: ' + JSON.stringify(lstorage, null, 2) + '\n'
    display_credentials.innerText += 'expiresIn: '  + authResult.expiresIn  +   ' expiresAt: ' + new Date(parseInt(expiresAt)) + " Now -> " + new Date() + '\n'

    web_AUTH.idToken =idToken;
    web_AUTH.accessToken =accessToken;
    web_AUTH.expiresAt = expiresAt;

  }

  function renewTokens() {
    webAuth.checkSession({}, (err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        localLogin(authResult);
      } else if (err) {
        alert(
            'Could not get a new token '  + err.error + ':' + err.error_description + '.'
        );
        logout();
      }
      displayButtons();
    });
  }

  function logout() {
    // Remove isLoggedIn flag from localStorage
    localStorage.removeItem('isLoggedIn');
    // Remove tokens and expiry time
    accessToken = '';
    idToken = '';
    expiresAt = 0;

    webAuth.logout({
      return_to: window.location.origin
    });

    displayButtons();
  }

  function isAuthenticated() {
    // Check whether the current time is past the
    // Access Token's expiry time
    var expiration = parseInt(expiresAt) || 0;
    return localStorage.getItem('isLoggedIn') === 'true' && new Date().getTime() < expiration;
  }


  const foo = () => console.log('Foo!');

  function displayButtons() {
    if (isAuthenticated()) {
      loginBtn.style.display = 'none';
      logoutBtn.style.display = 'inline-block';

    const btnId = "btnId"
    //   loginStatus.innerHTML = 'You are logged in! <br> Now you can request other services!' ;
    //   loginStatus.innerHTML = `You are logged in! <br> Now you can request other services! <br> <button id=${btnId}> ReqAPI </button> `;


    } else {
      loginBtn.style.display = 'inline-block';
      logoutBtn.style.display = 'none';
      loginStatus.innerHTML =
        'You are not logged in! Please log in to continue.';
    }
  }

  if (localStorage.getItem('isLoggedIn') === 'true') {

	console.log('localStorage >', localStorage.getItem('isLoggedIn'));

    renewTokens();
  } else {
    handleAuthentication();
  }

	console.log('START  >');

});


