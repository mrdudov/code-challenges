import { elements } from "./elements.js"
import {
  card_holder_validator,
  card_number_validator,
  cvc_validator,
  month_validator,
  year_validator,
} from "./validators.js"

import "./style.css"

elements.confirm_btn.onclick = () => {
  const card_holder = elements.inputs.card_holder.value
  const card_number = elements.inputs.card_number.value
  const cvc = elements.inputs.cvc.value
  const month = elements.inputs.exp_date_mm.value
  const year = elements.inputs.exp_date_yy.value

  const card_holder_errors = card_holder_validator(card_holder)
  const card_number_errors = card_number_validator(card_number)
  const cvc_errors = cvc_validator(cvc)
  const exp_errors = month_validator(month).concat(year_validator(year))

  if (card_holder_errors.length !== 0) {
    elements.errors.card_holder.classList.remove('hidden')
    elements.errors.card_holder.innerHTML = card_holder_errors[0]
  } else {
    elements.errors.card_holder.classList.add('hidden')
  }

  if (card_number_errors.length !== 0) {
    elements.errors.card_number.classList.remove('hidden')
    elements.errors.card_number.innerHTML = card_number_errors[0]
  } else {
    elements.errors.card_number.classList.add('hidden')
  }

  if (cvc_errors.length !== 0) {
    elements.errors.cvc.classList.remove('hidden')
    elements.errors.cvc.innerHTML = cvc_errors[0]
  } else {
    elements.errors.cvc.classList.add('hidden')
  }

  if (exp_errors.length !== 0) {
    elements.errors.exp_date.classList.remove('hidden')
    elements.errors.exp_date.innerHTML = exp_errors[0]
  } else {
    elements.errors.exp_date.classList.add('hidden')
  }

}
