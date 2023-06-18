import "./styles/styles.css"

import { SignUpComponent } from "./components/sign_up/sign_up.component.js"

const sign_up_container = document.querySelector("#sign-up")

const sign_up_component = new SignUpComponent()

sign_up_container.innerHTML += sign_up_component.get_html()
