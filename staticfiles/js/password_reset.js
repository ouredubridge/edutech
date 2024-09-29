document.addEventListener('DOMContentLoaded', function () {
    
    // Add functionality for `password` eye icon
    document.querySelector('.togglePassword').addEventListener('click', function() {

        const passwordField = document.getElementById('id_new_password1');
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';

        passwordField.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    })

    // Add functionality for `confirm password` eye icon
    document.querySelector('.toggleConfirmPassword').addEventListener('click', function() {

        const passwordField = document.getElementById('id_new_password2');
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';

        passwordField.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    })

    // Check terms and conditions functionality
    document.querySelector('.termsAndConditions').addEventListener('change', function() {
        document.querySelector('.submitButton').disabled = !this.checked;
    });

})