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
    const daysInMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0).getDate();
    const firstDayOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1).getDay();
    const currentMonth = currentDate.toLocaleDateString('default', {month: 'short'});

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
                checkbox.name = `date-${dayNumber}`;
                checkbox.id = `date-${dayNumber}`;

                if (dayNumber < currentDate.getDate() && currentDate.getMonth() === currentDate.getMonth()) {
                    checkbox.disabled = true;
                }

                const label = document.createElement('label');
                label.classList.add('calendar__day-number');
                label.textContent = dayNumber;
                label.setAttribute('for', `date-${dayNumber}`);

                tableCell.appendChild(checkbox);
                tableCell.appendChild(label);

                if (dayNumber === currentDate.getDate() && currentDate.getMonth() === currentDate.getMonth()) {
                    tableCell.classList.add('current-day');
                }
            } else if (dayNumber <= 0) {
                // Display the last days of the previous month
                const prevMonthDayNumber = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0).getDate() + dayNumber;
                const checkbox = document.createElement('input');
                checkbox.classList.add('visually-hidden');
                checkbox.type = 'checkbox';
                checkbox.name = `date-${prevMonthDayNumber}`;
                checkbox.id = `date-${prevMonthDayNumber}`;
                checkbox.disabled = true;

                const label = document.createElement('label');
                label.classList.add('calendar__day-number', 'prev-month');
                label.textContent = prevMonthDayNumber;
                label.setAttribute('for', `date-${prevMonthDayNumber}`);

                tableCell.appendChild(checkbox);
                tableCell.appendChild(label);
            } else {
                // Display the first days of the next month
                const nextMonthDayNumber = dayNumber - daysInMonth;
                const checkbox = document.createElement('input');
                checkbox.classList.add('visually-hidden');
                checkbox.type = 'checkbox';
                checkbox.name = `date-${nextMonthDayNumber}`;
                checkbox.id = `date-${nextMonthDayNumber}`;

                const label = document.createElement('label');
                label.classList.add('calendar__day-number', 'next-month');
                label.textContent = nextMonthDayNumber;
                label.setAttribute('for', `date-${nextMonthDayNumber}`);

                tableCell.appendChild(checkbox);
                tableCell.appendChild(label);
            }


            tableRow.appendChild(tableCell);
            dayNumber++;
        }

        calendarTableBody.appendChild(tableRow);
        dayOfWeek = (dayOfWeek + 1) % 7;
    }

    const currentMonthYear = document.querySelector('.current-month-year');
    const currentMonthName = currentDate.toLocaleDateString('default', {month: 'short'});
    currentMonthYear.textContent = `${currentMonthName} ${currentDate.getFullYear()}`;
});