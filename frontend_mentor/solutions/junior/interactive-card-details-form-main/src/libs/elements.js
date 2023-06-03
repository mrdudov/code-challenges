export { get_elements }

function get_elements() {
  return {
    card_holder: {
      input: document.querySelector("#cardholder"),
      output: document.querySelector("#card-name"),
      error: document.querySelector("#cardholder-error"),
    },
    card_number: {
      input: document.querySelector("#card-number"),
      output: document.querySelector("#card-code"),
      error: document.querySelector("#card-number-error"),
    },
    cvc: {
      input: document.querySelector("#cvc-input"),
      output: document.querySelector("#card-cvc"),
      error: document.querySelector("#cvc-error"),
    },
    exp_date_mm: {
      input: document.querySelector("#exp-date-mm"),
      output: document.querySelector("#exp-date-mm-out"),
      error: document.querySelector("#exp-date-error"),
    },
    exp_date_yy: {
      input: document.querySelector("#exp-date-yy"),
      output: document.querySelector("#exp-date-yy-out"),
      error: document.querySelector("#exp-date-error"),
    },
    buttons: {
      confirm: document.querySelector("#confirm-btn"),
      continue: document.querySelector("#continue-btn"),
    },
    blocks: {
      form: document.querySelector("#form"),
      complete: document.querySelector(".complete"),
    },
  }
}
