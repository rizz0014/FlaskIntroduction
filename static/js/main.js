// page date
window.onload = function getYear() {
    let currentYear = new Date().getFullYear();
    let pageYear = document.getElementById('currentYear');
  
    pageYear.innerHTML = currentYear;
  };
