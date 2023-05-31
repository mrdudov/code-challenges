export { FormComponent }

import { get_elements } from "./elements.js"
import {
  card_holder_validator,
  card_number_validator,
  cvc_validator,
  month_validator,
  year_validator,
} from "../../libs/validators.js"
import { on_validation } from "../../libs/functions.js"

import "./form.component.css"
import html from "./form.component.html"

class FormComponent {
  constructor() {}
  get_html() {
    return html
  }
  after_dom() {
    const elements = get_elements(document)

    elements.buttons.confirm.onclick = () => {
      const card_holder = elements.inputs.card_holder.value
      const card_number = elements.inputs.card_number.value
      const cvc = elements.inputs.cvc.value
      const month = elements.inputs.exp_date_mm.value
      const year = elements.inputs.exp_date_yy.value

      const card_holder_errors = card_holder_validator(card_holder)
      const card_number_errors = card_number_validator(card_number)
      const cvc_errors = cvc_validator(cvc)
      const exp_errors = month_validator(month).concat(year_validator(year))

      on_validation(card_holder_errors, elements.errors.card_holder)
      on_validation(card_number_errors, elements.errors.card_number)
      on_validation(cvc_errors, elements.errors.cvc)
      on_validation(exp_errors, elements.errors.exp_date)

      const all_error = []
        .concat(card_holder_errors)
        .concat(card_number_errors)
        .concat(exp_errors)
        .concat(cvc_errors)

      if (all_error.length === 0) {
        elements.blocks.form.classList.add("hidden")
        elements.blocks.complete.classList.remove("hidden")
      }
    }
  }
}
