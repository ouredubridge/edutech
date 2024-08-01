document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.querySelector('.menu-icon');
    const nav = document.querySelector('nav ul');

    const selectButton = document.querySelector('.select-button');
    const chevron = selectButton.querySelector('.chevron-down');

    selectButton.addEventListener('click', () => {
        chevron.classList.toggle('chevron-up')
    })


    menuIcon.addEventListener('click', function() {
	nav.classList.toggle('active');
    });
    alert("I'm working")
});
