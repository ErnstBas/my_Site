// Source: https://dev.to/ljcdev/easy-hamburger-menu-with-js-2do0

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const menuItems = document.querySelectorAll('.menuItem');

    menuItems.forEach(item => {
      if (item.getAttribute('href') === currentPath) {
        item.classList.add('active');
      }
    });
  });
</script>
