import "./styles/styles.css"

import { data } from "./data.js"

const chart = document.querySelector(".chart")

const max = Math.max(...data.map((item) => item.amount))

data.forEach((day) => {
  let height = (100 * day.amount) / max
  chart.innerHTML += `
        <div class="chart-item">
            <div class="${
              day.amount === max ? "chart-item-max-column" : "chart-item-column"
            }" style="height:${height}%;"></div>
            <p class="cart-title">${day["day"]}</p>
        </div>
    `
})
