document.addEventListener('DOMContentLoaded', function(){
    let expField = document.querySelector('#amtField');
    let expFieldFeedback = document.querySelector('#amtFieldFeedback');
    let dateField = document.querySelector("#dateField");
    let dateFieldFeedback = document.querySelector('#dateFieldFeedback');
    let categoryField = document.querySelector('#categoryField');
    let addExpButton = document.querySelector('#addExpButton');
    let descriptionField = document.querySelector('#descriptionField');
    let descriptionFieldFeedback = document.querySelector('#descriptionFieldFeedback');
    let valid1 = false;
    let valid2 = false;
    let valid3 = false;
    let valid4 = false;
    let now = new Date();
    now.setHours(0,0,0,0);
    addExpButton.disabled = true;
    console.log("hello");

    //username field validator.
    expField.addEventListener("keyup", function(letter){
        let expVal = letter.target.value;
                if (!isNumeric(expVal)){
                    expField.classList.add('is-invalid');
                    expFieldFeedback.innerHTML = '<p>Please enter a valid number for expense value.</p>';
                    expFieldFeedback.style.display = 'block';
                    valid1 = false;
                }
                else {
                    expField.classList.remove('is-invalid');
                    expFieldFeedback.style.display = 'none';
                    valid1 = true;
                }

            if (valid1 && valid2 && valid3 && valid4){
                addExpButton.disabled = false;
            }
    
            else if (!(valid1 && valid2 && valid3)){
                addExpButton.disabled = true;
            }
        }
    );

    dateField.addEventListener("change", function(){
        let val = new Date(dateField.value);
            if (val > now){
                dateField.classList.add('is-invalid');
                dateFieldFeedback.innerHTML = '<p>Please enter a valid date.</p>';
                dateFieldFeedback.style.display = 'block';
                valid2 = false;
            }
            else{
                dateField.classList.remove('is-invalid');
                dateFieldFeedback.style.display = 'none';
                valid2 = true;
            }

            if (valid1 && valid2 && valid3 && valid4){
                addExpButton.disabled = false;
            }
    
            else if (!(valid1 && valid2 && valid3 && valid4)){
                addExpButton.disabled = true;
            }

        });

   
    categoryField.addEventListener("change", function(){
        console.log(categoryField.value);
        if (categoryField.value === null){
            valid3 = false;
        }
        else{
            valid3 = true;
        }

        if (valid1 && valid2 && valid3 && valid4){
            addExpButton.disabled = false;
        }

        else if (!(valid1 && valid2 && valid3 && valid4)){
            addExpButton.disabled = true;
        }
    })


    descriptionField.addEventListener("keyup", function(letter){
        let des = letter.target.value;
        if (des.length > 256){
            dateFieldFeedback.style.display = 'block';
            descriptionField.classList.add('is-invalid');
            descriptionFieldFeedback.innerHTML = `Character max over limit. ${256 - des.length}`;
            descriptionFieldFeedback.style.display = 'block';
            valid4 = false;
        }

        else {
            descriptionField.classList.remove('is-invalid');
            descriptionFieldFeedback.style.display = 'none'
            valid4 = true;
        }
    });


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

    function isNumeric(str) {
        if (typeof str != "string") return false // we only process strings!  
            return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
                   !isNaN(parseFloat(str)) // ...and ensure strings of whitespace fail
        }
});