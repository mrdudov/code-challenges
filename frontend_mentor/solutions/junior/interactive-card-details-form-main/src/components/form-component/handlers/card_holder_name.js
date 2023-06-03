export { card_holder_name_handler }

import validator from "validator"

import { on_validation } from "../../../libs/functions.js"
import { CARD_HOLDER_NAME_DEFAULT } from "../../../config.js"

function card_holder_name_handler(element) {
  const card_holder = element.input.value
  const errors = card_holder_validator(card_holder)
  on_validation(errors, element, card_holder, CARD_HOLDER_NAME_DEFAULT)
  return errors
}

function card_holder_validator(name) {
  const error_messages = []
  if (validator.isEmpty(name)) {
    error_messages.push("Empty string")
  }
  for (let n_part of name.trim().split(/\s+/)) {
    if (!validator.isEmpty(n_part) && !validator.isAlpha(n_part)) {
      error_messages.push("Invalid name")
    }
  }
  return error_messages
}
