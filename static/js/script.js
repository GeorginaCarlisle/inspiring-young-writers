// Load page before adding event listeners
window.onload = function() {
    // Call function to check if a close confirmation is needed
    closeConfirmNeeded();

    // Add click event listener to the mobile nav hamburger
    let openNav = document.getElementById("nav-open");
    openNav.addEventListener('click', mobileNav);

    // Add click event listener to Parent info link in desktop nav
    let parentInfoOpen = document.getElementById("parent-info-open");
    parentInfoOpen.addEventListener('click', parentInfo);

    // Add click event listener to Parent info link in mobile nav
    let infoParentOpen = document.getElementById("info-parent-open");
    infoParentOpen.addEventListener('click', parentInfoMobile);

    // Call function to check if html being loaded is sign-up form
    inSignup();
    }
  
/**
 * Called when the hamburger is clicked. Click event Listener activated on load.
 * Mobile navigation displayed block and visible. Aria-hidden changed to false.
 * Click event listener added to nav-closed button with anonymous function to hide modal
 * and re-vert changes to style and aria-hidden.
 */
function mobileNav() {
    // Display mobile navigation
    let navigation = document.getElementById("mobile-nav");
    navigation.style.display = "block";
    navigation.setAttribute('aria-hidden', 'false');
    // Add click event listener to close symbol that re-hides modal
    let closeCross = document.getElementById("nav-closed");
    closeCross.onclick = function() {
        // Hide mobile nav
        navigation.setAttribute('aria-hidden', 'true');
        navigation.style.display = "none";
        };
    }

/**
 * Called when the 'Parent' button in the desktop nav or link from the sign-up form is clicked. 
 * Click event Listener activated on load. 
 * Parent info displayed flex and visible. Aria-hidden changed to false.
 * Click event listener added to parent-info-closed button with anonymous function to hide modal
 * and re-vert changes to style and aria-hidden.
 */
function parentInfo() {
    // Display information for parents
    let information = document.getElementById("parent-info-modal");
    information.style.display = "flex";
    information.setAttribute('aria-hidden', 'false');
    // Add click event listener to close symbol that re-hides modal
    let closeCross = document.getElementById("parent-info-closed");
    closeCross.onclick = function() {
        // Hide parent information
        information.setAttribute('aria-hidden', 'true');
        information.style.display = "none";
        };
    }

/**
 * Called when the 'Parent' button in the mobile nav is clicked. Click event Listener activated on load.
 * Parent info displayed flex and visible. Aria-hidden changed to false. Mobile nav is closed
 * Click event listener added to parent-info-closed button with anonymous function to hide modal
 * and re-vert changes to style and aria-hidden.
 */
function parentInfoMobile() {
    // Display information for parents
    let information = document.getElementById("parent-info-modal");
    information.style.display = "flex";
    information.setAttribute('aria-hidden', 'false');
    let navigation = document.getElementById("mobile-nav");
    navigation.style.display = "none";
    // Add click event listener to close symbol that re-hides modal
    let closeCross = document.getElementById("parent-info-closed");
    closeCross.onclick = function() {
        // Hide parent information
        information.setAttribute('aria-hidden', 'true');
        information.style.display = "none";
        };
    }

/**
 * Called on window loading
 * If there is a close button needing a confirmation message (found in create_writing.html and edit_writing.html)
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
            confirmModal.setAttribute('aria-hidden', 'false');
            // event listener for keep writing
            let keepWriting = document.getElementById("keep-writing");
            keepWriting.addEventListener('click', function(){
                // re-hide modal
                confirmModal.style.display = "none";
                confirmModal.setAttribute('aria-hidden', 'true');
                })
            });
        }
    }

/**
 * Called on window loading
 * If the current page is signup.html and therefore the 'open-parent-info' can be found
 * an event listener will be added to this element which on clicking will
 * call the parentInfo function
 */
function inSignup() {
    if (document.getElementById("open-parent-info")) {
        let openParentInfo = document.getElementById("open-parent-info");
        openParentInfo.addEventListener('click', parentInfo);
    }
}
