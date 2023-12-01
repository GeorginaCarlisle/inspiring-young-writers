// Load page before adding event listeners
window.onload = function() {
    // Add click event listener to the mobile nav hamburger
    let openNav = document.getElementById("nav-open");
    openNav.addEventListener('click', mobileNav);
  };
  
/**
 * Called when the hamburger is clicked. Click event Listener activated on load.
 * Mobile navigation displayed block and visible. 
 * Click event listener added to nav-closed button with anonymous function to hide modal.
 */
function mobileNav() {
    // Display mobile navigation
    let navigation = document.getElementById("mobile-nav");
    navigation.style.display = "block";
    // Add click event listener to close symbol that re-hides modal
    let closeCross = document.getElementById("nav-closed");
    closeCross.onclick = function() {
      // Hide mobile nav
      navigation.style.display = "none";
    };
  }