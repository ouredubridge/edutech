document.addEventListener('DOMContentLoaded', function() {
    // Menu icon button
    const menuIcon = document.querySelector('.menu-icon');

    // Nav Div
    const nav = document.querySelector('nav');

    // Dropdown button
    const dropDownButton = document.querySelector('.dropdown-button');
    // Dropdown contents
    const dropDownContent = document.querySelector('.dropdown-content');

    // Chevron down button
    const chevron = dropDownButton.querySelector('.chevron-down');

    // Dropdown behavior
    dropDownButton.addEventListener('click', () => {
        chevron.classList.toggle('chevron-up');
        dropDownContent.classList.toggle('show');
    });

    // Menu icon behavior
    menuIcon.addEventListener('click', function() {
	    nav.classList.toggle('active');
        menuIcon.classList.toggle('open')
    });

    // Hide the menu when clicking outside the menu
    document.addEventListener('click', (event) => {
        if (!nav.contains(event.target) && !menuIcon.contains(event.target)) {
          nav.classList.remove('active');
          menuIcon.classList.remove('open')
        }
    });
});
