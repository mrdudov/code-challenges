export { FormComponent }

import { get_elements } from "../../libs/elements.js"
import { card_holder_name_handler } from "./handlers/card_holder_name.js"
import { card_number_handler } from "./handlers/card_number.js"
import { cvc_handler } from "./handlers/cvc.js"
import { month_handler } from "./handlers/month.js"
import { year_handler } from "./handlers/year.js"
import { has_no_errors } from "../../libs/functions.js"

import "./form.component.css"
import html from "./form.component.html"

class FormComponent {
  get_html() {
    return html
  }
  after_dom() {
    const elements = get_elements()

    elements.buttons.confirm.onclick = () => {
      const has_no_any_error = has_no_errors([
        card_holder_name_handler(elements.card_holder),
        card_number_handler(elements.card_number),
        cvc_handler(elements.cvc),
        month_handler(elements.exp_date_mm),
        year_handler(elements.exp_date_yy),
      ])

      if (has_no_any_error) {
        elements.blocks.form.classList.add("hidden")
        elements.blocks.complete.classList.remove("hidden")
      }
    }
  }
}
