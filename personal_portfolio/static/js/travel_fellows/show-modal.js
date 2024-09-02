export const showModalPopup = (messageType, message) => {
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