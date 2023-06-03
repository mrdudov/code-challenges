export { month_handler }

import validator from "validator"

import { on_validation } from "../../../libs/functions.js"

function month_handler(element) {
  const month = element.input.value
  const errors = month_validator(month)
  on_validation(errors, element.error, element.output, month)
  return errors
}

function month_validator(month) {
  const error_messages = []
  if (validator.isEmpty(month)) {
    error_messages.push("Empty string")
  }
  if (!validator.isInt(month, { min: 1, max: 12 })) {
    error_messages.push("must be number in [1, 12]")
  }
  return error_messages
}
