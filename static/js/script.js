// Load page before adding event listeners
window.onload = function() {
    // Add click event listener to the mobile nav hamburger
    let openNav = document.getElementById("nav-open");
    openNav.addEventListener('click', mobileNav);

    // Call function to check if a close confirmation is needed
    closeConfirmNeeded()
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

/**
 * Called on window loading
 * If there is a close button needing a confirmation message
 * a modal providing message and choice to go back or keep writing will
 * appear on clicking of the button
 */
function closeConfirmNeeded() {
    if (document.getElementById("back-button")) {
        let backButton = document.getElementById("back-button");
        backButton.addEventListener('click', function(event){
            event.preventDefault();
            // display modal
            let confirmModal = document.getElementById("confirm-modal");
            confirmModal.style.display = "block";
            // event listener for keep writing
            let keepWriting = document.getElementById("keep-writing");
            keepWriting.addEventListener('click', function(){
                // re-hide modal
                confirmModal.style.display = "none";
            })
        });
    }
}
