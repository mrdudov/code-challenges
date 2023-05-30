export { elements }

const elements = {
  inputs: {
    card_holder: document.querySelector("#cardholder"),
    card_number: document.querySelector("#card-number"),
    exp_date_mm: document.querySelector("#exp-date-mm"),
    exp_date_yy: document.querySelector("#exp-date-yy"),
    cvc: document.querySelector("#cvc-input"),
  },
  outputs: {
    card_code: document.querySelector("#card-code"),
    card_name: document.querySelector("#card-name"),
    card_exp_date: document.querySelector("#card-exp-date"),
    cvc: document.querySelector("#card-cvc"),
  },
  confirm_btn: document.querySelector("#confirm-btn"),

  errors: {
    card_holder: document.querySelector("#cardholder-error"),
    card_number: document.querySelector("#card-number-error"),
    exp_date: document.querySelector("#exp-date-error"),
    cvc: document.querySelector("#cvc-error"),
  },
}
