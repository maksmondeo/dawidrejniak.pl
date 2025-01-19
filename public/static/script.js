const lenis = new Lenis();

lenis.on('scroll', (e) => {
  console.log(e);
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.section-5-pytanie-header').forEach(header => {
      header.addEventListener('click', () => {

          const parent = header.parentElement;
          const icon = parent.querySelector('.icon');
          const answer = parent.querySelector('.section-5-pytanie-answer');
          
          parent.classList.toggle('open');

          if (parent.classList.contains('open')) {
              icon.textContent = '-';
          } else {
              icon.textContent = '+'; 
          }
      });
  });
});

document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {
      var notification = document.getElementById("full-screen-message");
      if (notification) {
          notification.classList.add("fade-out");
          setTimeout(function() {
              notification.classList.add("hidden");
          }, 500);
      }
  }, 3000);
});