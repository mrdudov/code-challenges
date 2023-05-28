const email_el = document.querySelector('#email')
const error_img = document.querySelector('#error-img')
const error_msg = document.querySelector('#error-msg')

function send_email_btn() {
    email = email_el.value
    
    if (email_validator(email)){
        send_email()
    } else {
        error_img.style.display = 'block'
        error_msg.style.display = 'block'
    }


}


function email_validator(email) {
    const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (email.match(validRegex)) {
        return true
    }
    return false
}

function send_email() {
    console.log('email send')
    email_el.value = ''
    error_img.style.display = 'none'
    error_msg.style.display = 'none'
}