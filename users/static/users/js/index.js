document.addEventListener('DOMContentLoaded', function () {
    
    // Add functionality for `password` eye icon
    document.querySelector('.togglePassword').addEventListener('click', function() {

        const passwordField = document.getElementById('password');
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';

        passwordField.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    })

    // Add functionality for `confirm password` eye icon
    document.querySelector('.toggleConfirmPassword').addEventListener('click', function() {

        const passwordField = document.getElementById('confirmPassword');
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';

        passwordField.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    })

    // Check terms and conditions functionality
    document.querySelector('.termsAndConditions').addEventListener('change', function() {
        document.querySelector('.submitButton').disabled = !this.checked;
    });

    // Elements for `terms and conditions` popup functionality
    const openPopupBtn = document.getElementById('openTermsPopup');
    const termsPopup = document.getElementById('termsPopup');
    const acceptTermsBtn = document.getElementById('acceptTerms');
    const declineTermsBtn = document.getElementById('declineTerms');
    const termsCheckbox = document.getElementById('termsAndConditions')
    const submitButton = document.getElementById('signup-button');

    // Open the popup
    openPopupBtn.addEventListener('click', (e) => {
        e.preventDefault();
        termsPopup.style.display = 'flex';
    })

    // Accept terms
    acceptTermsBtn.addEventListener('click', () => {
        termsCheckbox.checked =  true; // Check the checkbox
        termsPopup.style.display = 'none'; // Close the popup
        submitButton.disabled = false // Enable the submit button
    })

    // Decline terms
    declineTermsBtn.addEventListener('click', () => {
        termsPopup.style.display = 'none'; // Close the popup
    })
})