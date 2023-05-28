const first_name_input = document.querySelector('#first-name')
const last_name_input = document.querySelector('#last-name')
const email_input = document.querySelector('#email')
const password_input = document.querySelector('#password')

const first_name_error_img = document.querySelector('#first-name+img')
const last_name_error_img = document.querySelector('#last-name+img')
const email_error_img = document.querySelector('#email+img')
const password_error_img = document.querySelector('#password+img')

const first_name_error_msg = document.querySelector('#first-name-error-msg')
const last_name_error_msg = document.querySelector('#last-name-error-msg')
const email_error_msg = document.querySelector('#email-error-msg')
const password_error_msg = document.querySelector('#password-error-msg')

function email_validator(email) {
    const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (email.match(validRegex)) {
        return true
    }
    return false
}

function claim_btn() {

    let valid_first_name_flag = false
    let valid_last_name_flag = false
    let valid_email_flag = false
    let valid_password_flag = false

    if (first_name_input.value === '') {
        first_name_error_msg.style.display = 'block'
        first_name_error_img.style.display = 'block'
        valid_first_name_flag = false
    } else {
        first_name_error_msg.style.display = 'none'
        first_name_error_img.style.display = 'none'
        valid_first_name_flag = true     
    }

    if (last_name_input.value === '') {
        last_name_error_msg.style.display = 'block'
        last_name_error_img.style.display = 'block'
        valid_last_name_flag = false
    } else {
        last_name_error_msg.style.display = 'none'
        last_name_error_img.style.display = 'none'
        valid_last_name_flag = true     
    }

    if (email_input.value === '') {
        email_error_msg.style.display = 'block'
        email_error_img.style.display = 'block'
        email_error_msg.innerHTML = 'Email cannot be empty'
        valid_email_flag = false
    } else if (email_validator(email_input.value)) {
        email_error_msg.style.display = 'none'
        email_error_img.style.display = 'none'
        valid_email_flag = true     
    } else {
        email_error_msg.style.display = 'block'
        email_error_img.style.display = 'block'
        email_error_msg.innerHTML = 'Looks like this is not en email'
        valid_email_flag = false
    }
    
    if (password_input.value === '') {
        password_error_msg.style.display = 'block'
        password_error_img.style.display = 'block'
        valid_password_flag = false
    } else {
        password_error_msg.style.display = 'none'
        password_error_img.style.display = 'none'
        valid_password_flag = true     
    }

    if (valid_first_name_flag 
        && valid_last_name_flag
        && valid_email_flag
        && valid_password_flag
        ) {
            console.log('msg send')
        }

} 
