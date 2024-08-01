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
            input.value = value + 1;
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const currentDate = new Date();
    let displayedDate = new Date(currentDate)
    const previousMonth = document.querySelector('.calendar__control--prev');
    const nextMonth = document.querySelector('.calendar__control--next');

    function renderCalendar() {
        const daysInMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth(), 0).getDate();
        const firstDayOfMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth() - 1, 1).getDay();
        const currentMonth = displayedDate.toLocaleDateString('default', {month: 'long'});

        const calendarTableBody = document.querySelector('.calendar__table-body');
        calendarTableBody.innerHTML = '';

        let dayOfWeek = 0; // Start from Sunday
        let dayNumber = 1 - firstDayOfMonth; // Adjust for the first day of the month

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
                    checkbox.name = `${currentMonth}-${dayNumber}`;
                    checkbox.id = `${currentMonth}-${dayNumber}`;
                    if (dayNumber === currentDate.getDate()) {
                        checkbox.checked = true;
                    }

                    if (dayNumber < currentDate.getDate() && currentDate.getMonth() === currentDate.getMonth()) {
                        checkbox.disabled = true;
                    }

                    const label = document.createElement('label');
                    label.classList.add('calendar__day-number');
                    label.textContent = dayNumber;
                    label.setAttribute('for', `${currentMonth}-${dayNumber}`);

                    tableCell.appendChild(checkbox);
                    tableCell.appendChild(label);

                    if (dayNumber === currentDate.getDate() && currentDate.getMonth() === currentDate.getMonth()) {
                        tableCell.classList.add('current-day');
                    }
                } else if (dayNumber <= 0) {
                    // Display the last days of the previous month
                    const prevMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth(), 0);
                    const prevMonthName = prevMonth.toLocaleString('default', {month: 'long'});
                    const prevMonthDayNumber = prevMonth.getDate() + dayNumber
                    const checkbox = document.createElement('input');
                    checkbox.classList.add('visually-hidden');
                    checkbox.type = 'checkbox';
                    checkbox.name = `${prevMonthName}-${prevMonthDayNumber}`;
                    checkbox.id = `${prevMonthName}-${prevMonthDayNumber}`;
                    checkbox.disabled = true;

                    const label = document.createElement('label');
                    label.classList.add('calendar__day-number', 'prev-month');
                    label.textContent = prevMonthDayNumber;
                    label.setAttribute('for', `${prevMonthName}-${prevMonthDayNumber}`);

                    tableCell.appendChild(checkbox);
                    tableCell.appendChild(label);
                } else {
                    // Display the first days of the next month
                    const nextMonthDayNumber = dayNumber - daysInMonth;
                    const checkbox = document.createElement('input');
                    const nextMonth = new Date(displayedDate.getFullYear(), displayedDate.getMonth()+1, 1);
                    const nextMonthName = nextMonth.toLocaleString('default', {month: 'long'});

                    checkbox.classList.add('visually-hidden');
                    checkbox.type = 'checkbox';
                    checkbox.name = `${nextMonthName}-${nextMonthDayNumber}`;
                    checkbox.id = `${nextMonthName}-${nextMonthDayNumber}`;

                    const label = document.createElement('label');
                    label.classList.add('calendar__day-number', 'next-month');
                    label.textContent = nextMonthDayNumber;
                    label.setAttribute('for', `${nextMonthName}-${nextMonthDayNumber}`);
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
        date.innerText = `${displayedDate.toLocaleString('default', {month: 'long'})} ${displayedDate.getFullYear()}`
    }


    renderCalendar()

    previousMonth.addEventListener('click', function() {
        displayedDate.setMonth(displayedDate.getMonth()-1);
        renderCalendar()
    })

    nextMonth.addEventListener('click', function() {
        displayedDate.setMonth(displayedDate.getMonth()+1);
        renderCalendar()
    })


});