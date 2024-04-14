document.addEventListener("DOMContentLoaded", function() {
  const currentPage = window.location.pathname.split('/').pop();
  const menuItems = document.querySelectorAll('.menu a[href]');

  menuItems.forEach(item => {
    const itemPage = item.getAttribute('href').split('/').pop();

    if (itemPage === currentPage) {
      item.classList.add('current');
      const submenuContainer = item.closest('.submenu-container');
      if (submenuContainer) {
        submenuContainer.classList.add('open');
      }
    }
  });
});
