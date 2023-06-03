export { card_number_handler }

import validator from "validator"
import { on_validation } from "../../../libs/functions.js"

function card_number_handler(element) {
  const card_number = element.input.value
  const errors = card_number_validator(card_number)
  on_validation(errors, element.error, element.output, by_four(card_number))
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

function by_four(in_str) {
  const arr = String(in_str).split("")
  const result = []
  for (let i = 0; i < arr.length; i++) {
    if (i % 4 === 0) {
      result.push(" ")
    }
    result.push(arr[i])
  }
  return result.join("").trim()
}
