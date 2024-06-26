const nav = document.querySelector(".page-nav");
const navToggle = document.querySelector(".page-nav__toggler");
const headerContent = document.querySelector(".page-header__content-wrapper");

nav.classList.remove("page-nav--no-js");

navToggle.addEventListener("click", function() {
  nav.classList.toggle("page-nav--active");
  nav.classList.toggle("page-nav--inactive");
  nav.classList.add("page-nav--white");
  if (scrollY === 0 && nav.classList.contains("page-nav--inactive")) {
    nav.classList.remove("page-nav--white");
  }
});

window.addEventListener("scroll", function() {
  nav.classList.add("page-nav--white");
  nav.classList.add("page-nav--scrolled");
  nav.classList.remove(".page-nav--inner");
  if (scrollY === 0 && nav.classList.contains("page-nav--inactive")) {
    nav.classList.remove("page-nav--white");
    nav.classList.remove("page-nav--scrolled");
    nav.classList.add("page-nav--inner");
  }
});
