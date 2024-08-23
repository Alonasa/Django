const countrySelectButton = document.querySelector(".country-select--choose");
const countryDeleteButton = document.querySelector(".plan-step__delete-country--removable");
const countrySelectPopup = document.querySelector(".chose-country");
const choseCountryLink = document.querySelectorAll(".chose-country__country-link");
const countrySelector = document.querySelector(".plan-step__country-selector");
const addCountry = document.querySelector(".country-select--add");
const plansContainer = document.querySelector('.plan-step__selects');
let countriesData = {}
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

const fetchAsync = async (url) => {
    let response = await fetch(url);
    let data = await response.json();
    return data;
}

const fetchCountryCodes = async () => {
    try {
        const url = 'http://localhost:8000/portfolio/fellows/countries-data/';
        const data = await fetchAsync(url);
        const countryCodes = data;
        return {success: true, data: countryCodes};
    } catch (error) {
        console.error('Error fetching country codes:', error);
        return {success: false, error: error.message};
    }
}

const getCountries = () => {
    fetchCountryCodes().then(res => {
        if (res.success) {
            countriesData = res.data
            return countriesData
        } else {
            console.error(res.error)
        }
    })
}

document.addEventListener('DOMContentLoaded', getCountries)

choseCountryLink.forEach((el) => el.addEventListener("click", function (event) {
    event.preventDefault();
    const text = event.currentTarget.textContent;
    const planSteps = document.querySelectorAll(".plan-step__select-wrapper");
    const countryCode = countriesData[text];
    console.log(planSteps)

    const newElement =
        `
                    <button class="country-select country-select--chosen" type="button">
                        ${text}
                    </button>
                    <div class="plan-step__flag-wrapper plan-step__flag-wrapper--active">
                        <div class="country-flag country-flag--big" data-tooltip="${text}">
                            <span class="country-flag__picture flag-square ip2location-flag-32 ip2location-flag-64 flag-${countryCode}"></span>
                        </div>
                    </div>
                    <button class="plan-step__delete-country" type="button">
                        <span class="visually-hidden">Remove country</span>
                    </button>
                `;

    if (planSteps.length > 0) {
        let element = Array.from(planSteps).filter((el) => el.dataset.tooltip === text)
        if (element.length + 1 < 2) {
            const newElementNode = document.createElement('div');
            newElementNode.classList.add('plan-step__select-wrapper');
            newElementNode.dataset.tooltip = text;
            newElementNode.innerHTML = newElement;
            const lastElement = planSteps[0];
            lastElement.parentNode.insertBefore(newElementNode, lastElement);
            getCountriesData();
            countrySelector.style.display = "none";
            createDescription(text, countryCode)
        } else {
            showModalPopup("info", "You are already have this country in your travel plan")
        }
    }
}))


function showModalPopup(messageType, message) {
    const modal = document.createElement('div');
    modal.classList.add('modal');

    const modalContent = document.createElement('div');
    modalContent.classList.add('modal-content');
    if (messageType === "error") {
        modalContent.classList.add('modal-error');
    } else if (messageType === "info") {
        modalContent.classList.add('modal-info');
    }

    modalContent.textContent = message;

    modal.appendChild(modalContent);

    document.body.appendChild(modal);
    setTimeout(() => {
        modal.remove()
    }, 3000)

    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.remove();
        }
    });
}


const createDescription = (countryName, countryFlag) => {
    const parentElement = document.querySelector('.plan-step__description-wrapper');

    const planConent =
        `
            <div class="plan-step__description-title">
                <label class="plan-step__description-label" for="${countryFlag}-plans">${countryName}
                </label>
                <div class="country-flag country-flag--big" data-tooltip="${countryName}">
                    <span class="country-flag__picture  flag-square ip2location-flag-32 ip2location-flag-64 flag-${countryFlag}"></span>
                </div>
            </div>
            <div class="plan-step__plan-description-wrapper">
                <textarea class="plan-step__plan-description" id="${countryFlag}-plans"
                                                      placeholder="Plan" required=""></textarea>
                <div class="plan-step__plan-description-invalid">
                    This field must be filled
                </div>
            </div>                       
        `
    const tempElement = document.createElement('div');
    tempElement.classList.add('plan-step__country-description');
    tempElement.innerHTML = planConent;
    parentElement.appendChild(tempElement);
}


plansContainer.addEventListener("click", function (event) {
    const countryDescriptions = document.querySelectorAll('.plan-step__country-description')
    const parentElement = event.target.parentElement;
    const countryName = parentElement.dataset.tooltip;

    if (event.target.classList.contains("plan-step__delete-country")) {
        parentElement.remove();
        countryDescriptions.forEach(description => {
            const descriptionCountryName = description.querySelector('.country-flag').dataset.tooltip;
            if (descriptionCountryName === countryName) {
                description.remove();
            }
        })
    }
});


addCountry.addEventListener("click", function () {
    countrySelector.style.display = "flex";
})

