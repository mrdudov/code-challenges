import { elements } from "./elements.js"

import "./style.css"

console.log(elements)

elements.confirm_btn.onclick = () => {
  console.log("confirm-btn-click")
}
