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