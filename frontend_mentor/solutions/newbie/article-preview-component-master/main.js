const share_btn = document.querySelector('#share-btn')
const show_toggle = document.querySelector('#show-toggle')

is_show = false

if (is_show) {
    show_toggle.style.display ='block'
} else {
    show_toggle.style.display ='none'
}


share_btn.onclick = () => {
    is_show = !is_show
    if (is_show) {
        show_toggle.style.display ='block'
    } else {
        show_toggle.style.display ='none'
    }
}

