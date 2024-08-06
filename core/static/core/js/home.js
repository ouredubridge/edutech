document.addEventListener('DOMContentLoaded', function () {
  /* JS Functionality for the courses div section */
  const container = document.querySelector('.courses-section-div');
  const leftArrow = document.querySelector('.arrow-left');
  const rightArrow = document.querySelector('.arrow-right');


  const scrollAmount = 300;

  leftArrow.addEventListener('click', () => {
    container.scrollBy({
        left: -scrollAmount,
        behavior: 'smooth'
    });
  });

  rightArrow.addEventListener('click', () => {
    container.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
    });
  });

  /*// Show Scrollbar on Hover
  container.addEventListener('mouseover', () => {
    container.style.overflowX = 'scroll';
  });

  // Hide the scrollbar on mouseout
  container.addEventListener('mouseout', () => {
    container.style.overflowX = 'hidden';
  });*/

})