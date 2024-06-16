const nameContact = document.querySelector('#nameContact');
const emailContact = document.querySelector('#emailContact');
const phoneContact = document.querySelector('#phoneContact')
const message = document.querySelector('#message');
const sendSubmit = document.querySelector('#formContact button[type="submit"]')
const formContact = document.querySelector('#formContact');

const contact = {
    name: '',
    email: '',
    phone: '',
    message: ''
}


document.addEventListener('DOMContentLoaded', () => {

    nameContact.addEventListener('input', validateNameContact);

    emailContact.addEventListener('input', validateEmailContact);

    phoneContact.addEventListener('input', validatePhoneContact);

    message.addEventListener('input', validateMessage);

    formContact.addEventListener('submit', checkFormContact);

})

const validateNameContact = ({ target }) => {

    const nameLength = target.value.trim().length;
    const feedbackAlert = document.querySelector('#feedbackNameContact');
    const feedbackMessage = nameLength >= 7 ? '' : 'The name should have 7 or more characters';
    const isValid = nameLength >= 7;

    if (!feedbackAlert) {
        const feedback = document.createElement('div');
        feedback.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');
        feedback.id = 'feedbackNameContact';
        feedback.innerHTML = feedbackMessage;

        nameContact.classList.remove('is-valid', 'is-invalid');
        nameContact.classList.add(isValid ? 'is-valid' : 'is-invalid');

        target.parentElement.appendChild(feedback);
    } else {
        feedbackAlert.innerHTML = feedbackMessage;
        feedbackAlert.classList.remove(isValid ? 'invalid-feedback' : 'valid-feedback');
        feedbackAlert.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');

        nameContact.classList.remove(isValid ? 'is-invalid' : 'is-valid');
        nameContact.classList.add(isValid ? 'is-valid' : 'is-invalid');
    }

    if (isValid) {
        contact['name'] = target.value
        validateFormContact()
    } else {
        contact['name'] = ''
        validateFormContact()
    }
};

const validateEmailContact = ({ target }) => {
    const regex = /^\S+@\S+\.\S+$/;
    const email = target.value.trim();
    const isValid = regex.test(email);
    const feedbackAlert = document.querySelector('#feedbackemailContact');
    const feedbackMessage = isValid ? '' : 'Enter a valid email ex: example@gmail.com';

    if (!feedbackAlert) {
        const feedback = document.createElement('div');
        feedback.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');
        feedback.id = 'feedbackemailContact';
        feedback.innerHTML = feedbackMessage;

        emailContact.classList.remove('is-valid', 'is-invalid');
        emailContact.classList.add(isValid ? 'is-valid' : 'is-invalid');


        target.parentElement.appendChild(feedback);
    } else {
        feedbackAlert.innerHTML = feedbackMessage;
        feedbackAlert.classList.remove(isValid ? 'invalid-feedback' : 'valid-feedback');
        feedbackAlert.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');

        emailContact.classList.remove(isValid ? 'is-invalid' : 'is-valid');
        emailContact.classList.add(isValid ? 'is-valid' : 'is-invalid');
    }

    if (isValid) {
        contact['email'] = target.value
        validateFormContact()
    } else {
        contact['email'] = ''
        validateFormContact()
    }
}


const validatePhoneContact = ({ target }) => {
    const phoneLength = target.value.trim().length;
    const feedbackAlert = document.querySelector('#feedbackPhoneContact');
    const feedbackMessage = phoneLength > 1 ? '' : 'Minimum characters 1';
    const isValid = phoneLength > 1;

    if (!feedbackAlert) {
        const feedback = document.createElement('div');
        feedback.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');
        feedback.id = 'feedbackPhoneContact';
        feedback.innerHTML = feedbackMessage;

        phoneContact.classList.remove('is-valid', 'is-invalid');
        phoneContact.classList.add(isValid ? 'is-valid' : 'is-invalid');


        target.parentElement.appendChild(feedback);
    } else {
        feedbackAlert.innerHTML = feedbackMessage;
        feedbackAlert.classList.remove(isValid ? 'invalid-feedback' : 'valid-feedback');
        feedbackAlert.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');

        phoneContact.classList.remove(isValid ? 'is-invalid' : 'is-valid');
        phoneContact.classList.add(isValid ? 'is-valid' : 'is-invalid');
    }

    if (isValid) {
        contact['phone'] = target.value
        validateFormContact()
    } else {
        contact['phone'] = ''
        validateFormContact()
    }
}


const validateMessage = ({ target }) => {

    const messageLength = target.value.trim().length;
    const feedbackAlert = document.querySelector('#feedbackMessageContact');
    const feedbackMessage = messageLength > 19 ? '' : 'Minimum characters 20';
    const isValid = messageLength > 19;

    if (!feedbackAlert) {
        const feedback = document.createElement('div');
        feedback.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');
        feedback.id = 'feedbackMessageContact';
        feedback.innerHTML = feedbackMessage;

        message.classList.remove('is-valid', 'is-invalid');
        message.classList.add(isValid ? 'is-valid' : 'is-invalid');


        target.parentElement.appendChild(feedback);
    } else {
        feedbackAlert.innerHTML = feedbackMessage;
        feedbackAlert.classList.remove(isValid ? 'invalid-feedback' : 'valid-feedback');
        feedbackAlert.classList.add(isValid ? 'valid-feedback' : 'invalid-feedback');

        message.classList.remove(isValid ? 'is-invalid' : 'is-valid');
        message.classList.add(isValid ? 'is-valid' : 'is-invalid');
    }

    if (isValid) {
        contact['message'] = target.value
        validateFormContact()
    } else {
        contact['message'] = ''
        validateFormContact()
    }
};


const validateFormContact = () => {
    if (!Object.values(contact).includes("")) {
        sendSubmit.disabled = false;
        return;
    }
    sendSubmit.disabled = true
}
const checkFormContact = (event) => {
    event.preventDefault();
    console.log('enviando correo')
}