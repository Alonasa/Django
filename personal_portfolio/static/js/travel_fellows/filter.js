const filter = document.querySelector(".filter");
const filterToggler = filter.querySelector(".filter__toggler");
const filterRegions = filter.querySelector(".filter__region-list");
const filterTogglerText = filter.querySelector(".filter__toggler-text");
const filterInner = filter.querySelector(".filter__inner");
const filterButtonClose = filter.querySelector(".filter__inner-button-close");

filterToggler.addEventListener("click", function() {
  filterToggler.classList.toggle("filter__toggler--open");
  filterToggler.classList.toggle("filter__toggler--close");
  filterInner.classList.toggle("filter__inner--active");

  if (document.documentElement.clientWidth < 768) {
    filterRegions.classList.toggle("filter__region-list--active");
  }
});

filterButtonClose.addEventListener("click", function() {
  filterToggler.classList.add("filter__toggler--open");
  filterToggler.classList.remove("filter__toggler--close");
  filterInner.classList.remove("filter__inner--active");

  if (document.documentElement.clientWidth < 768) {
    filterRegions.classList.remove("filter__region-list--active");
  }
});

window.addEventListener("keydown", function(event) {
  if (event.keyCode === 27) {
    filterToggler.classList.add("filter__toggler--open");
    filterToggler.classList.remove("filter__toggler--close");
    filterInner.classList.remove("filter__inner--active");

    if (document.documentElement.clientWidth < 768) {
      filterRegions.classList.remove("filter__region-list--active");
    }
  }
});
