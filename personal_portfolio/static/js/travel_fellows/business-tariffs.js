document.addEventListener('DOMContentLoaded', function () {

    const businessPopupOpen = document.querySelector(".add-profile__business-link");
    const businessPopup = document.querySelector(".business-popup");
    const businessPopupClose = document.querySelector(".business-popup__close-button");

    if (businessPopupOpen) {
      businessPopupOpen.addEventListener("click", function (event) {
        event.preventDefault();
        businessPopup.classList.add("business-popup--active");
      });
    }

    if (businessPopupClose) {
      businessPopupClose.addEventListener("click", function () {
        businessPopup.classList.remove("business-popup--active");
      });
    }

    window.addEventListener("keydown", function (event) {
        if (event.keyCode === 27) {
            businessPopup.classList.remove("business-popup--active");
        }
    });
})
