document.addEventListener('DOMContentLoaded', function () {
  alert("Welcome to EduBridge")
  /* Initialize AOS */
  AOS.init({
    duration: 1200,
    offset: 200,
    /*once: true*/
  });

  /* ScrollReveal */
  ScrollReveal().reveal('.reveal', {
    distance: '50px',
    duration: 1000,
    easing: 'ease-in-out',
    origin: 'bottom',
    reset: true // Optional: Reset animation when element leaves viewport
  }); 

  /* Parameters for the courses div section */
  const container = document.querySelector('.courses-section-div');
  const leftArrow = document.querySelector('.arrow-left');
  const rightArrow = document.querySelector('.arrow-right');

  /* Parameters for top categories div section */
  const scrollContainer = document.querySelector('.top-categories-scrollable-div');
  const scrollItems = document.querySelectorAll('.top-category-div');

  /* JS Functionality for the courses div section */
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

  /* JS functionality for top categories div section */
  scrollContainer.addEventListener('scroll', () => {
    alert("Inside the if statement")
    scrollItems.forEach(item => {
      const rect = item.getBoundingClientRect();
      const containerRect = scrollContainer.getBoundingClientRect();

      if (rect.left >= containerRect.left && rect.right <= containerRect.right) {
        item.classList.add('scrolled');
        
      } else {
        item.classList.remove('scrolled');
      }
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