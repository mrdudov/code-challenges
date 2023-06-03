export { card_number_handler }

import validator from "validator"
import { on_validation } from "../../../libs/functions.js"
import { CARD_NUMBER_DEFAULT } from "../../../config.js"
import { by_four } from "../../../libs/functions.js"

function card_number_handler(element) {
  const card_number = element.input.value
  const errors = card_number_validator(card_number)
  on_validation(
    errors,
    element,
    by_four(card_number),
    by_four(CARD_NUMBER_DEFAULT)
  )
  return errors
}

function card_number_validator(card_number) {
  const error_messages = []
  if (validator.isEmpty(card_number)) {
    error_messages.push("Empty string")
  }
  if (!validator.isCreditCard(card_number)) {
    error_messages.push("Invalid card number")
  }
  return error_messages
}
