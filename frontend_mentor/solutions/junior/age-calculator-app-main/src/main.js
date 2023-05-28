import {    
    is_required,
    is_number,
    is_less_then,
    is_greater_then,
    validator
} from "./libs/validators.js"

import './style.css'

import { calculate_age } from './libs/calculate_age.js'


const day_block = document.querySelector('#day-input-block')
const month_block = document.querySelector('#month-input-block')
const year_block = document.querySelector('#year-input-block')

const calc_btn = document.querySelector('#calculate-age')

const display_day = document.querySelector('#display-day')
const display_month = document.querySelector('#display-month')
const display_year = document.querySelector('#display-year')

const display_delta = document.querySelector('#display-delta')

function mark_input_block(messages, block) {
    if (messages.length === 0) {
        block.classList.remove('validation-error')
        block.querySelector('.error-msg-container').innerHTML = ''
        block.querySelector('input').classList.remove('input-validation-error')
    } else {
        block.classList.add('validation-error')
        block.querySelector('.error-msg-container').innerHTML = messages[0]
        block.querySelector('input').classList.add('input-validation-error')
    }
}

calc_btn.onclick = () => {
    const day_validation = validator(day_block.querySelector('#day').value.trim(), [
        {
            "validator_fn": is_required,
            "is_critical": true
        }, {
            "validator_fn": is_number,
            "is_critical": true,
            "post_fn": parseInt
        }, {
            "validator_fn": is_less_then,
            "validator_fu_args": {
                "less_then": 1
            }
        }, {
            "validator_fn": is_greater_then,
            "validator_fu_args": {
                "great_then": 31
            }
        }
    ])

    const month_validation = validator(month_block.querySelector('#month').value.trim(), [
        {
            "validator_fn": is_required,
            "is_critical": true
        }, {
            "validator_fn": is_number,
            "is_critical": true,
            "post_fn": parseInt
        }, {
            "validator_fn": is_less_then,
            "validator_fu_args": {
                "less_then": 1
            }
        }, {
            "validator_fn": is_greater_then,
            "validator_fu_args": {
                "great_then": 12
            }
        }
    ])

    const year_validation = validator(year_block.querySelector('#year').value.trim(), [
        {
            "validator_fn": is_required,
            "is_critical": true
        }, {
            "validator_fn": is_number,
            "is_critical": true,
            "post_fn": parseInt
        }, {
            "validator_fn": is_less_then,
            "validator_fu_args": {
                "less_then": 100
            }
        }, {
            "validator_fn": is_greater_then,
            "validator_fu_args": {
                "great_then": new Date().getFullYear()
            }
        }
    ])

    mark_input_block(day_validation["messages"], day_block)
    mark_input_block(month_validation["messages"], month_block)
    mark_input_block(year_validation["messages"], year_block)

    const all_messages = day_validation["messages"]
        .concat(month_validation["messages"])
        .concat(year_validation["messages"])

    if (all_messages.length === 0) {
        const age_delta = calculate_age({
            'year': year_validation["value"],
            'month': month_validation["value"],
            'day': day_validation["value"]
        })

        display_day.innerHTML = age_delta['day']
        display_month.innerHTML = age_delta['month']
        display_year.innerHTML = age_delta['year']
    } else {
        display_day.innerHTML = '--'
        display_month.innerHTML = '--'
        display_year.innerHTML = '--'
    }
}
