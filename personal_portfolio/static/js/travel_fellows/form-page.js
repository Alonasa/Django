document.addEventListener('DOMContentLoaded', function () {
    const decreaseButtons = document.querySelectorAll('.plan-step__number-input-button--decrease');
    const increaseButtons = document.querySelectorAll('.plan-step__number-input-button--increase');

    decreaseButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const inputId = this.dataset.input;
            const input = document.getElementById(inputId);
            let value = parseInt(input.value);
            if (value > input.min) {
                input.value = value - 1;
            }
        });
    });

    increaseButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const inputId = this.dataset.input;
            const input = document.getElementById(inputId);
            let value = parseInt(input.value);
            if (value < input.max) {
                input.value = value + 1;
            }
        });
    });
});


let todaysDate

const checkboxDisable = (dayNumber, currentDate, selectedMonth, year, checkbox) => {
    let dat = new Date()
    if (dayNumber < currentDate.getDate() && currentDate.getMonth() === selectedMonth && year === dat.getFullYear()) {
        checkbox.disabled = true;
    }
}

const setDisabled = (displayedDate, currentDate, checkbox) => {
    if (displayedDate < currentDate) {
        checkbox.disabled = true;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const currentDate = new Date();
    let displayedDate = new Date(currentDate.getTime());
    const previousMonth = document.querySelector('.calendar__control--prev');
    const nextMonth = document.querySelector('.calendar__control--next');

    function renderCalendar(selectedMonth) {
        const daysInMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth(), 0).getDate();
        const firstDayOfMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth(), 1).getDay();
        const currentMonth = displayedDate.toLocaleDateString('default', {month: 'long'});
        const month = new Date().toLocaleDateString('default', {month: 'long'});
        const calendarTableBody = document.querySelector('.calendar__table-body');
        calendarTableBody.innerHTML = '';
        let dayOfWeek = 0;
        let dayNumber = 1 - firstDayOfMonth;
        let selectedYear = displayedDate.getFullYear();
        let currentMonthNumber = displayedDate.getMonth() + 1;

        while (dayNumber <= daysInMonth + (6 - ((firstDayOfMonth + daysInMonth - 1) % 7))) {
            const tableRow = document.createElement('tr');

            tableRow.classList.add('calendar__table-row');
            for (let i = 0; i < 7; i++) {
                const tableCell = document.createElement('td');


                tableCell.classList.add('calendar__table-cell');
                if (dayNumber > 0 && dayNumber <= daysInMonth) {
                    const checkbox = document.createElement('input');
                    checkbox.classList.add('visually-hidden');
                    checkbox.type = 'checkbox';
                    checkbox.name = 'picked-date'
                    checkbox.value = `${currentMonthNumber}-${dayNumber}-${displayedDate.getFullYear()}`;
                    checkbox.id = `${currentMonthNumber}-${dayNumber}-${displayedDate.getFullYear()}`;
                    todaysDate = `${currentMonthNumber}-${dayNumber}-${displayedDate.getFullYear()}`;
                    if (dayNumber === currentDate.getDate() && currentMonth === month && currentDate.getFullYear() === displayedDate.getFullYear()) {
                        checkbox.checked = true;
                        todaysDate = `${currentMonthNumber}-${dayNumber}-${displayedDate.getFullYear()}`;
                    }
                    setDisabled(displayedDate, currentDate, checkbox)

                    if (selectedMonth === undefined) {
                        selectedMonth = currentDate.getMonth();
                        checkboxDisable(dayNumber, currentDate, selectedMonth, selectedYear, checkbox)
                    } else {
                        checkboxDisable(dayNumber, currentDate, selectedMonth, selectedYear, checkbox)
                    }

                    const label = document.createElement('label');
                    label.classList.add('calendar__day-number');
                    label.textContent = dayNumber.toString();
                    label.setAttribute('for', `${currentMonthNumber}-${dayNumber}-${displayedDate.getFullYear()}`);
                    tableCell.appendChild(checkbox);
                    tableCell.appendChild(label);

                    if (currentDate === displayedDate) {
                        tableCell.classList.add('current-day');
                    } else {
                        tableCell.classList.remove('current-da')
                    }

                } else if (dayNumber <= 0) {
                    const prevMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth(), 0);
                    const prevMonthName = prevMonth.getMonth() + 1;
                    const prevMonthDayNumber = prevMonth.getDate() + dayNumber;
                    const checkbox = document.createElement('input');
                    checkbox.classList.add('visually-hidden');
                    checkbox.type = 'checkbox';
                    checkbox.name = 'picked-date';
                    checkbox.value = `${prevMonthName}-${prevMonthDayNumber}-${displayedDate.getFullYear()}`;
                    checkbox.id = `${prevMonthName}-${prevMonthDayNumber}-${displayedDate.getFullYear()}`;
                    if (month === currentMonth && currentDate.getFullYear() === selectedYear || displayedDate < currentDate) {
                        checkbox.disabled = true;
                    }

                    const label = document.createElement('label');
                    label.classList.add('calendar__day-number', 'prev-month');
                    label.textContent = prevMonthDayNumber.toString();
                    label.setAttribute('for', `${prevMonthName}-${prevMonthDayNumber}-${displayedDate.getFullYear()}`);
                    tableCell.appendChild(checkbox);
                    tableCell.appendChild(label);
                } else {
                    const nextMonthDayNumber = dayNumber - daysInMonth;
                    const checkbox = document.createElement('input');
                    const nextMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth() + 1, 1);
                    const nextMonthName = nextMonth.getMonth() + 1;

                    checkbox.classList.add('visually-hidden');
                    checkbox.type = 'checkbox';
                    checkbox.name = 'picked-date'
                    checkbox.value = `${nextMonthName}-${nextMonthDayNumber}-${displayedDate.getFullYear()}`;
                    checkbox.id = `${nextMonthName}-${nextMonthDayNumber}-${displayedDate.getFullYear()}`;
                    setDisabled(displayedDate, currentDate, checkbox)


                    const label = document.createElement('label');
                    label.classList.add('calendar__day-number', 'next-month');
                    label.textContent = nextMonthDayNumber.toString();
                    label.setAttribute('for', `${nextMonthName}-${nextMonthDayNumber}-${displayedDate.getFullYear()}`);
                    tableCell.appendChild(checkbox);
                    tableCell.appendChild(label);
                }


                tableRow.appendChild(tableCell);
                dayNumber++;
            }

            calendarTableBody.appendChild(tableRow);
            dayOfWeek = (dayOfWeek + 1) % 7;
        }

        const date = document.querySelector('.calendar__title');
        date.innerText = `${currentMonth} ${selectedYear}`
        return todaysDate
    }

    renderCalendar()
    datesPicker()

    previousMonth.addEventListener('click', function () {
        let month = displayedDate.getMonth() - 1;
        displayedDate.setMonth(month);
        renderCalendar(month);
        datesPicker();
    })

    nextMonth.addEventListener('click', function () {
        let month = displayedDate.getMonth() + 1;
        displayedDate.setMonth(month);
        renderCalendar(month);
        datesPicker();
    })
});


const uncheckCheckboxes = (elements) => {
    elements.forEach(d => {
        d.checked = false
    });
}

const datesPicker = () => {
    let datesList = document.querySelectorAll('.calendar__day-number');
    let datesCheckboxes = document.querySelectorAll('.calendar__table-cell input');
    let dates = [];
    let counter = 0;


    datesList.forEach(el => {
        el.addEventListener('click', () => {
            let currentId = el.getAttribute('for');
            counter += 1;
            switch (counter) {
                case 1: {
                    dates = [];
                    dates[0] = currentId;
                    uncheckCheckboxes(datesCheckboxes)
                    break
                }
                case 2: {
                    let oldChoice = new Date(dates[0].replace("-", " "));
                    let newChoice = new Date(currentId.replace("-", " "));
                    if (newChoice < oldChoice) {
                        dates[0] = currentId;
                        counter = 1;
                        uncheckCheckboxes(datesCheckboxes)
                        return counter
                    } else {
                        dates[1] = currentId
                    }
                    counter = 0
                    return counter
                }
            }
        })
    })
};
