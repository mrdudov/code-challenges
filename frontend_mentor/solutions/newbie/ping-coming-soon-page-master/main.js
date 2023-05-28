function email_validator(email) {
    const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (email.match(validRegex)) {
        return true
    }
    return false
}

const email_input_el = document.querySelector('form div input')
const error_msg = document.querySelector('#error-msg')



function notify_me_btn() {
    if (email_validator(email_input_el.value)){
        error_msg.style.display = 'none'
    } else {
        error_msg.style.display = 'block'
    }
}
