document.addEventListener('DOMContentLoaded', function(){
    const emailRe = /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$/;
    let emailField = document.querySelector('#emailField');
    let emailFieldFeedback = document.querySelector('#emailFieldFeedback');
    let showPasswordButton = document.querySelector('#showPassword');
    let loginButton = document.querySelector('#loginButton');
    let valid1 = false;
    let valid2 = false;
    showPasswordButton.style.cursor = 'pointer';
    loginButton.disabled = true;

    //email field validator
    emailField.addEventListener("keyup", function(letter){

        let emailVal = letter.target.value;
        if (!emailRe.test(emailVal)){
                    emailField.classList.add('is-invalid');
                    emailFieldFeedback.innerHTML = `<p> Email is not valid. </p>`;
                    emailFieldFeedback.style.display = 'block';
                    valid1 = false;
                }

                else {
                    emailField.classList.remove('is-invalid');
                    emailFieldFeedback.style.display = 'none';
                    valid1 = true;
                }

        if (valid1 && valid2){
            loginButton.disabled = false;
        }

        else if (!(valid1 && valid2)){
            loginButton.disabled = true;
        }

        }
    );

    passwordField.addEventListener("keyup", function(letter){

        let passVal = letter.target.value;

        if (passVal.length >= 8){
                passwordField.classList.remove('is-invalid');
                passwordFieldFeedback.style.display = 'none';
                valid2 = true;
            }

        else {
            passwordField.classList.add('is-invalid');
            passwordFieldFeedback.innerHTML = `<p> Password must be atleast 8 characters.</p>`;
            passwordFieldFeedback.style.display = 'block';
            valid2 = false;
        }

        if (valid1 && valid2){
            loginButton.disabled = false;
        }

        else if (!(valid1 && valid2)){
            loginButton.disabled = true;
        }

    });

    showPasswordButton.addEventListener("click", function(){
        if (showPasswordButton.textContent == "SHOW PASSWORD"){
            showPasswordButton.textContent = "HIDE";
            passwordField.setAttribute("type", "text");
        }
        else{
            showPasswordButton.textContent = "SHOW PASSWORD";
            passwordField.setAttribute("type", "password");
        }
    })

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;}

});