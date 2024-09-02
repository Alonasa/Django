import { showModalPopup } from "./show-modal.js";

const countrySelectButton = document.querySelector(".country-select--choose");
const countryDeleteButton = document.querySelector(".plan-step__delete-country--removable");
const countrySelectPopup = document.querySelector(".chose-country");
const choseCountryLinks = document.querySelectorAll(".chose-country__country-link");
const countrySelector = document.querySelector(".plan-step__country-selector");
const addCountryButton = document.querySelector(".country-select--add");
const plansContainer = document.querySelector('.plan-step__selects');
const parentElement = document.querySelector('.plan-step__description-wrapper');
const step3 = document.querySelector('#step-3');
const planSteps = document.querySelectorAll(".plan-step__select-wrapper");
let countriesData = {};

const initCountrySelectPopup = () => {
    countrySelectButton.addEventListener("click", () => {
        togglePopup();
        toggleDeleteButton();
    });

    window.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closePopup();
        }
    });
};

const togglePopup = () => {
    countrySelectPopup.classList.toggle("chose-country--active");
    countrySelectButton.classList.toggle("country-select--blue");
};

const toggleDeleteButton = () => {
    if (document.documentElement.clientWidth < 768) {
        countryDeleteButton.classList.toggle("plan-step__delete-country--inactive");
    }
};

const closePopup = () => {
    countrySelectPopup.classList.remove("chose-country--active");
    countrySelectButton.classList.remove("country-select--blue");
    toggleDeleteButton();
};

const fetchCountryCodes = async () => {
    try {
        const response = await fetch('http://localhost:8000/portfolio/fellows/countries-data/');
        return { success: true, data: await response.json() };
    } catch (error) {
        console.error('Error fetching country codes:', error);
        return { success: false, error: error.message };
    }
};

const loadCountries = async () => {
    const result = await fetchCountryCodes();
    if (result.success) {
        countriesData = result.data;
    } else {
        console.error(result.error);
    }
};

const updateSelectedCountriesInput = () => {
    const countriesChosen = document.querySelectorAll(".country-select--chosen");
    const countriesList = Array.from(countriesChosen).map(country => country.textContent.trim());
    document.getElementById('selected-countries').value = countriesList.join(',');
};

const regulateSteps = (stepNumber) => {
    const steps = document.querySelectorAll(".plan-step__button-wrapper");
    step3.style.display = "block";
    steps[stepNumber].style.display = planSteps.length > 0 ? "flex" : "none";
};

const handleCountrySelection = (event) => {
    event.preventDefault();
    const countryName = event.currentTarget.textContent;
    const countryCode = countriesData[countryName];

    if (!countryCode) return;

    if (isCountryAlreadySelected(countryName)) {
        showModalPopup("info", "You already have this country in your travel plan");
        return;
    }

    addCountryElement(countryName, countryCode);
    updateSelectedCountriesInput();
    countrySelector.style.display = "none";
    regulateSteps(1);
};

const isCountryAlreadySelected = (countryName) => {
    return Array.from(planSteps).some(el => el.dataset.tooltip === countryName);
};

const addCountryElement = (countryName, countryCode) => {
    const newElementNode = document.createElement("div");
    newElementNode.classList.add("plan-step__select-wrapper");
    newElementNode.dataset.tooltip = countryName;
    newElementNode.innerHTML = createCountryElementHTML(countryName, countryCode);
    const lastElement = planSteps[0];
    lastElement.parentNode.insertBefore(newElementNode, lastElement);
    createDescription(countryName, countryCode);
    regulateSteps(1);
};

const createCountryElementHTML = (countryName, countryCode) => `
    <button class="country-select country-select--chosen" type="button">${countryName}</button>
    <div class="plan-step__flag-wrapper plan-step__flag-wrapper--active">
        <div class="country-flag country-flag--big" data-tooltip="${countryName}">
            <span class="country-flag__picture flag-square ip2location-flag-32 ip2location-flag-64 flag-${countryCode}"></span>
        </div>
    </div>
    <button class="plan-step__delete-country" type="button">
        <span class="visually-hidden">Remove country</span>
    </button>
`;

const createDescription = (countryName, countryFlag) => {
    const descriptionHTML = `
        <div class="plan-step__description-title">
            <label class="plan-step__description-label" for="${countryFlag}-plans">${countryName}</label>
            <div class="country-flag country-flag--big" data-tooltip="${countryName}">
                <span class="country-flag__picture flag-square ip2location-flag-32 ip2location-flag-64 flag-${countryFlag}"></span>
            </div>
        </div>
        <div class="plan-step__plan-description-wrapper">
            <textarea class="plan-step__plan-description" id="${countryFlag}-plans" name="${countryName}-plan" placeholder="Describe your plans for this trip" required></textarea>
            <div class="plan-step__plan-description-invalid">This field must be filled</div>
        </div>
    `;
    const tempElement = document.createElement('div');
    tempElement.classList.add('plan-step__country-description');
    tempElement.innerHTML = descriptionHTML;
    parentElement.appendChild(tempElement);
    regulateSteps(2);
};

const handleDeleteCountry = (event) => {
    if (event.target.classList.contains("plan-step__delete-country")) {
        const parentElement = event.target.closest('.plan-step__select-wrapper');
        const countryName = parentElement.dataset.tooltip;
        parentElement.remove();
        removeCountryDescription(countryName);
    }
};

const removeCountryDescription = (countryName) => {
    const descriptions = document.querySelectorAll('.plan-step__country-description');
    descriptions.forEach(description => {
        if (description.querySelector('.country-flag').dataset.tooltip === countryName) {
            description.remove();
        }
    });
};

const initEventListeners = () => {
    choseCountryLinks.forEach(link => link.addEventListener("click", handleCountrySelection));
    plansContainer.addEventListener("click", handleDeleteCountry);
    addCountryButton.addEventListener("click", () => {
        countrySelector.style.display = "flex";
    });
};

const init = async () => {
    await loadCountries();
    initCountrySelectPopup();
    initEventListeners();
};

document.addEventListener('DOMContentLoaded', init);