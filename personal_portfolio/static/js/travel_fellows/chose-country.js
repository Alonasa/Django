const countrySelectButton = document.querySelector(".country-select--choose");
const countryDeleteButton = document.querySelector(".plan-step__delete-country--removable");
const countrySelectPopup = document.querySelector(".chose-country");
const choseCountryLink = document.querySelectorAll(".chose-country__country-link");
const countrySelector = document.querySelector(".plan-step__country-selector");
const addCountry = document.querySelector(".country-select--add");
const deleteCountries = document.querySelectorAll(".plan-step__delete-country");
const plansContainer = document.querySelector('.plan-step__selects');

countrySelectButton.addEventListener("click", function () {
    countrySelectPopup.classList.toggle("chose-country--active");
    countrySelectButton.classList.toggle("country-select--blue");
    if (document.documentElement.clientWidth < 768) {
        countryDeleteButton.classList.toggle("plan-step__delete-country--inactive");
    }
});

window.addEventListener("keydown", function (event) {
    if (event.keyCode === 27) {
        countrySelectPopup.classList.remove("chose-country--active");
        countrySelectButton.classList.remove("country-select--blue");

        if (document.documentElement.clientWidth < 768) {
            countryDeleteButton.classList.remove("plan-step__delete-country--inactive");
        }
    }
});

const getCountriesData = () => {
    const countriesChosen = document.querySelectorAll(".country-select--chosen");
    const countriesList = Array.from(countriesChosen).map((country) => country.textContent.trim());

    const selectedCountriesInput = document.getElementById('selected-countries');
    selectedCountriesInput.value = countriesList.join(',');
}

choseCountryLink.forEach((el) => el.addEventListener("click", function (event) {
    event.preventDefault();
    const text = event.currentTarget.textContent;
    const planSteps = document.querySelectorAll(".plan-step__select-wrapper");
    const newFlag = `/static/img/travel_fellows/flag-${text.split(" ")[0].toLowerCase()}.svg`;

    const newElement =
        `
        <button class="country-select country-select--chosen" type="button">
            ${text}
        </button>
        <div class="plan-step__flag-wrapper plan-step__flag-wrapper--active">
            <div class="country-flag country-flag--big" data-tooltip="${text}">
                <img class="country-flag__picture"
                     src="${newFlag}"
                     alt="Flag ${text}"
                     width="35" height="24">
            </div>
        </div>
        <button class="plan-step__delete-country" type="button">
            <span class="visually-hidden">Remove country</span>
        </button>
    `;

    const newElementNode = document.createElement('div');
    newElementNode.classList.add('plan-step__select-wrapper');
    newElementNode.innerHTML = newElement;
    const lastElement = planSteps[0];
    lastElement.parentNode.insertBefore(newElementNode, lastElement);
    getCountriesData();
    countrySelector.style.display = "none";
}))



plansContainer.addEventListener("click", function(event) {
  if (event.target.classList.contains("plan-step__delete-country")) {
    const parentElement = event.target.parentElement;
    parentElement.remove();
  }
});


addCountry.addEventListener("click", function () {
    countrySelector.style.display = "flex";
})

