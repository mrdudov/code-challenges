import "./styles/common.css"
import "./styles/style.css"

import { FormComponent } from "./components/form-component/form.component.js"
import { CompleteComponent } from "./components/complete/complete.component.js"

const form_component = new FormComponent()
const complete_component = new CompleteComponent()

console.log(complete_component.get_html())

const form_area = document.querySelector(".form-area")

form_area.innerHTML += form_component.get_html()
form_area.innerHTML += complete_component.get_html()

form_component.after_dom()
complete_component.after_dom()
