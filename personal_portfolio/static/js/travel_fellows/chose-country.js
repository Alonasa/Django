const countrySelectButton = document.querySelector(".country-select--choose");
const countryDeleteButton = document.querySelector(".plan-step__delete-country--removable");
const countrySelectPopup = document.querySelector(".chose-country");
const choseCountryLink = document.querySelectorAll(".chose-country__country-link");
const countrySelector = document.querySelector(".plan-step__country-selector");
const addCountry = document.querySelector(".country-select--add");
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

async function fetchAsync(url) {
    let response = await fetch(url);
    let data = await response.json();
    return data;
}

async function fetchCountryCodes() {
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


choseCountryLink.forEach((el) => el.addEventListener("click", function (event) {
    event.preventDefault();
    const text = event.currentTarget.textContent;
    const planSteps = document.querySelectorAll(".plan-step__select-wrapper");
    let countriesData = {}

    fetchCountryCodes().then(res => {
        if (res.success) {
            countriesData = res.data
            console.log(countriesData)
            const newElement =
                `
                    <button class="country-select country-select--chosen" type="button">
                        ${text}
                    </button>
                    <div class="plan-step__flag-wrapper plan-step__flag-wrapper--active">
                        <div class="country-flag country-flag--big" data-tooltip="${text}">
                            <span class="country-flag__picture flag-square ip2location-flag-32 ip2location-flag-64 flag-${countriesData[text]}"></span>
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
        } else {
            console.error("Error fetching country codes:", res.error);
        }
    });
}))


plansContainer.addEventListener("click", function (event) {
    if (event.target.classList.contains("plan-step__delete-country")) {
        const parentElement = event.target.parentElement;
        parentElement.remove();
    }
});


addCountry.addEventListener("click", function () {
    countrySelector.style.display = "flex";
})

