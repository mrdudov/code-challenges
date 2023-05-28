import { notifications } from "./notifications_data_set.js"
import { notification_card } from "./src/notification_card.js"


const nt_container = document.querySelector('#notifications-container')
const nt_count_el = document.querySelector('#notifications-count')
const mark_all_as_read_btn = document.querySelector('#mark-all-as-read')

mark_all_as_read_btn.onclick = () => {
    for (const notification of notifications) {
        notification["is_read"] = true
    }
    render()
}

function render() {
    nt_container.innerHTML = ''
    let nt_count = 0;

    nt_count_el.innerHTML = nt_count
    
    for (const notification of notifications) {
        if (notification["is_read"] === false) {
            nt_count += 1
        }
        nt_container.append(notification_card(notification))
    }
    
    nt_count_el.innerHTML = nt_count
}

render()
