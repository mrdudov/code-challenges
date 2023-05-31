export { get_elements }

function get_elements(node) {
  return {
    inputs: {
      card_holder: node.querySelector("#cardholder"),
      card_number: node.querySelector("#card-number"),
      exp_date_mm: node.querySelector("#exp-date-mm"),
      exp_date_yy: node.querySelector("#exp-date-yy"),
      cvc: node.querySelector("#cvc-input"),
    },
    outputs: {
      card_code: node.querySelector("#card-code"),
      card_name: node.querySelector("#card-name"),
      card_exp_date: node.querySelector("#card-exp-date"),
      cvc: node.querySelector("#card-cvc"),
    },
    errors: {
      card_holder: node.querySelector("#cardholder-error"),
      card_number: node.querySelector("#card-number-error"),
      exp_date: node.querySelector("#exp-date-error"),
      cvc: node.querySelector("#cvc-error"),
    },
    buttons: {
      confirm: node.querySelector("#confirm-btn"),
      continue: node.querySelector("#continue-btn"),
    },
    blocks: {
      form: node.querySelector("#form"),
      complete: node.querySelector("#complete"),
    },
  }
}
