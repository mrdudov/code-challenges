import "./styles/common.css"
import "./styles/style.css"

import { FormComponent } from "./components/form-component/form.component.js"
import { CompleteComponent } from "./components/complete/complete.component.js"
import { CardsComponent } from "./components/cards/cards.component.js"

const form_component = new FormComponent()
const complete_component = new CompleteComponent()
const cards_component = new CardsComponent()

const form_area = document.querySelector(".form-area")
const img_area = document.querySelector(".img-area")


form_area.innerHTML += form_component.get_html()
form_area.innerHTML += complete_component.get_html()
img_area.innerHTML = cards_component.get_html()

form_component.after_dom()
complete_component.after_dom()
cards_component.after_dom()
