export { FormComponent }

import { get_elements } from "../../libs/elements.js"
import { card_holder_name_handler } from "./handlers/card_holder_name.js"
import { card_number_handler } from "./handlers/card_number.js"
import { cvc_handler } from "./handlers/cvc.js"
import { month_handler } from "./handlers/month.js"
import { year_handler } from "./handlers/year.js"
import { has_no_errors, by_four } from "../../libs/functions.js"

import {
  CARD_HOLDER_NAME_DEFAULT,
  CARD_NUMBER_DEFAULT,
  CVC_DEFAULT,
  MONTH_DEFAULT,
  YEAR_DEFAULT,
} from "../../config.js"

import "./form.component.css"
import html from "./form.component.html"

class FormComponent {

  get_html() {
    return html
  }
  init() {
    this.elements = get_elements()
    init_output_values(this.elements)
  }

  after_dom() {
    this.elements.buttons.confirm.onclick = () => {
      const has_no_any_error = has_no_errors([
        card_holder_name_handler(this.elements.card_holder),
        card_number_handler(this.elements.card_number),
        cvc_handler(this.elements.cvc),
        month_handler(this.elements.exp_date_mm),
        year_handler(this.elements.exp_date_yy),
      ])

      if (has_no_any_error) {
        this.elements.blocks.form.classList.add("hidden")
        this.elements.blocks.complete.classList.remove("hidden")
      }
    }
  }
}

function init_output_values(elements) {
  elements.card_holder.output.innerHTML = CARD_HOLDER_NAME_DEFAULT
  elements.card_number.output.innerHTML = by_four(CARD_NUMBER_DEFAULT)
  elements.cvc.output.innerHTML = CVC_DEFAULT
  elements.exp_date_mm.output.innerHTML = MONTH_DEFAULT
  elements.exp_date_yy.output.innerHTML = YEAR_DEFAULT
}
