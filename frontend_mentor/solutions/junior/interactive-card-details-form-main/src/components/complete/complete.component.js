export { CompleteComponent }

import { get_elements } from "../../libs/elements.js"

import html from "./complete.component.html"
import "./complete.component.css"

class CompleteComponent {
  constructor() {}
  get_html() {
    return html
  }
  after_dom() {
    const elements = get_elements()
    elements.buttons.continue.onclick = () => {
        console.log("continue btn")
    }
  }
}
