document.addEventListener('DOMContentLoaded', function(){
    const emailRe = /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$/;
    let passwordField = document.querySelector('#passwordField');
    let usernameField = document.querySelector('#usernameField');
    let usernameFieldFeedback = document.querySelector('#usernameFieldFeedback');
    let emailField = document.querySelector('#emailField');
    let emailFieldFeedback = document.querySelector('#emailFieldFeedback');
    let showPasswordButton = document.querySelector('#showPassword');
    let registerButton = document.querySelector('#registerButton');
    let valid1 = false;
    let valid2 = false;
    let valid3 = false;
    showPasswordButton.style.cursor = 'pointer';
    registerButton.disabled = true;

    //username field validator.
    usernameField.addEventListener("keyup", function(letter){
        let usernameVal = letter.target.value;
            fetch('/username_validation', {
                body: JSON.stringify({'username': usernameVal}), 
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                }
            }).then(res=>res.json())
            .then(data=>{
                if (data.username_error){
                    usernameField.classList.add('is-invalid');
                    usernameFieldFeedback.innerHTML = `<p>${data.username_error}</p>`;
                    usernameFieldFeedback.style.display = 'block';
                    valid1 = false;
                }
                else {
                    usernameField.classList.remove('is-invalid');
                    usernameFieldFeedback.style.display = 'none';
                    valid1 = true;
                }
            });

            if (valid1 && valid2 && valid3){
                registerButton.disabled = false;
            }
    
            else if (!(valid1 && valid2 && valid3)){
                registerButton.disabled = true;
            }
        }
    );

    //email field validator
    emailField.addEventListener("keyup", function(letter){

        let emailVal = letter.target.value;
        if (emailRe.test(emailVal)){

            fetch('/email_validation', {
                body: JSON.stringify({'email': emailVal}), 
                method: 'POST',
                csrfmiddlewaretoken: '{{ csrf_token }}',
                credentials: 'same-origin',
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                }
            }).then(res=>res.json())
            .then(data=>{
                if (data.email_error){
                    emailField.classList.add('is-invalid');
                    emailFieldFeedback.innerHTML = `<p>${data.email_error}</p>`;
                    emailFieldFeedback.style.display = 'block';
                    valid2 = false;
                }
                else {
                    emailField.classList.remove('is-invalid');
                    emailFieldFeedback.style.display = 'none';
                    valid2 = true;
                }
            });
    
        }
        else{
            emailField.classList.add('is-invalid');
            emailFieldFeedback.innerHTML = `<p> Email is not valid. </p>`;
            emailFieldFeedback.style.display = 'block';
            valid2 = false;
        }

        if (valid1 && valid2 && valid3){
            registerButton.disabled = false;
        }

        else if (!(valid1 && valid2 && valid3)){
            registerButton.disabled = true;
        }

        }
    );

    passwordField.addEventListener("keyup", function(letter){

        let passVal = letter.target.value;

        if (passVal.length >= 8){
                passwordField.classList.remove('is-invalid');
                passwordFieldFeedback.style.display = 'none';
                valid3 = true;
            }

        else {
            passwordField.classList.add('is-invalid');
            passwordFieldFeedback.innerHTML = `<p> Password must be atleast 8 characters.</p>`;
            passwordFieldFeedback.style.display = 'block';
            valid3 = false;
        }

        if (valid1 && valid2 && valid3){
            registerButton.disabled = false;
        }

        else if (!(valid1 && valid2 && valid3)){
            registerButton.disabled = true;
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