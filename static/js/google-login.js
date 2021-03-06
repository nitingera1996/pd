
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function onSignIn(googleUser) {
  //alert('Hello');
var profile = googleUser.getBasicProfile();
if(profile)
{
  onSignInClick(profile);
}
console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
console.log('Name: ' + profile.getName());
console.log('Image URL: ' + profile.getImageUrl());
console.log('Email: ' + profile.getEmail());
}

function onSignInClick(profile){
  var csrftoken = getCookie('csrftoken');
  if(profile.getImageUrl()==undefined){
    image_url="Set default image"
  }
  else{
    image_url=profile.getImageUrl();
  }
  $.ajax({
                  url : "/blogu/google_login/",
                  type : "POST",
                  dataType: "json",
                  data : {
                      email : profile.getEmail(),
                      name :  profile.getName(),
                      image_url: image_url,
                      id: profile.getId(),
                      'csrfmiddlewaretoken':csrftoken
                      },
                  success : function(json) {
                    console.log(json.response);
                    if(json.response=="logged in")
                    {
                      window.open("/","_self");
                    }
                  },
                  error : function(xhr,errmsg,err) {
                      alert(xhr.status + ": " + xhr.responseText);
                      //$('#email_error_msg').html(xhr.responseText);
                  }
              });
}
function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }
