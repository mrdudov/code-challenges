const question_msg = 'How did we do?'
const thank_msg = 'Thank you!'
const msg3 = `Please let us know how we did with your support request. All feedback is appreciated to help us improve our offering!`
const msg4 = 'You selected 4 out of 5'
const msg5 = `We appreciate you taking the time to give a rating. If you ever need more support, don’t hesitate to get in touch!`

const title = document.querySelector('#title')
const msg = document.querySelector('#msg')
const rating_buttons = document.querySelectorAll('#rating-btn button')
const rating_buttons_container = document.querySelector('#rating-btn')
const submit_btn = document.querySelector('#submit')
const thank_you_img = document.querySelector('#thank-you-img')
const star = document.querySelector('#star')
const rating_msg_container = document.querySelector('#rating-msg-container')
const selected_rating_p = document.querySelector('#rating-msg-container p')
const container = document.querySelector('#container')

title.innerText = question_msg
msg.innerText = msg3

rating_buttons.forEach((btn) => {
    btn.onclick = () => {
        rating_buttons.forEach((s_btn) => {
            s_btn.classList.remove('selected')
        })
        btn.classList.add('selected')
    }
})


submit_btn.onclick = () => {
    const selected_btn = document.querySelector('.selected')

    if (!selected_btn) {
        return
    }

    const rating = selected_btn.innerText
    const rating_msg = `You selected ${rating} out of 5`

    console.log(selected_rating_p)

    selected_rating_p.innerText = rating_msg
    
    rating_msg_container.style.display = 'flex'
    container.style.alignItems = 'center'
    star.style.display = 'none'
    submit_btn.style.display = 'none'
    rating_buttons_container.style.display = 'none'
    thank_you_img.style.display = 'block'
    title.innerText = thank_msg
    msg.style.textAlign = 'center'
    msg.innerText = msg5
}