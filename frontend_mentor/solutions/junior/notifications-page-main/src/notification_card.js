export function notification_card(notification) {
    const nt_card_el = document.createElement('div')
    nt_card_el.dataset.id = notification["id"]

    const card_right_cont = document.createElement('div')
    card_right_cont.classList.add("card-right-container")
    
    const age_el = document.createElement('p')
    age_el.classList.add('age')
    age_el.innerText = notification["age"]
    
    const avatar_img = document.createElement('img')
    avatar_img.src = notification["avatar"]
    avatar_img.classList.add("avatar-img")

    const name_el = document.createElement('span')
    name_el.classList.add('card-name')
    name_el.innerHTML = notification["name"]

    const type_msg = document.createElement('span')
    type_msg.classList.add('type-msg')
    type_msg.innerHTML = notification["type_msg"]

    nt_card_el.classList.add("notification-card")
    nt_card_el.append(avatar_img)
    
    card_right_cont.append(name_el)
    card_right_cont.append(type_msg)

    if (notification["message"]) {
        const message_el = document.createElement('span')
        message_el.classList.add('card-message')
        message_el.innerHTML = notification["message"]
        card_right_cont.append(message_el)
    }

    if (notification["msg_obj"]) {
        const msg_obj_el = document.createElement('span')
        msg_obj_el.classList.add('msg-obj')
        msg_obj_el.innerHTML = notification["msg_obj"]
        card_right_cont.append(msg_obj_el)
    }

    if (!notification["is_read"]) {
        nt_card_el.classList.add('un-read')
        const red_dot = document.createElement('div')
        red_dot.classList.add('red-dot')
        card_right_cont.append(red_dot)
    }

    card_right_cont.append(age_el)
    
    if (notification["private_msg"]) {
        const private_msg_el = document.createElement('p')
        private_msg_el.classList.add('private-msg')
        private_msg_el.innerHTML = notification["private_msg"]
        card_right_cont.append(private_msg_el)
    }
    
    nt_card_el.append(card_right_cont)
    if (notification["right_img"]) {
        const right_img = document.createElement('img')
        right_img.src = notification["right_img"]
        right_img.classList.add("right-img")
        nt_card_el.append(right_img)
    }
    
    return nt_card_el
}
