let password = document.querySelector('.password')

function copyPassword() {
    navigator.clipboard.writeText(password.textContent);
    alert('Password Copied')
}

password.addEventListener('click', copyPassword)