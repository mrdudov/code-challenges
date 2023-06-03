export { year_handler }

import validator from "validator"

import { on_validation } from "../../../libs/functions.js"
import { YEAR_DEFAULT } from "../../../config.js"

function year_handler(element) {
  const year = element.input.value
  const errors = year_validator(year)
  on_validation(errors, element, year, YEAR_DEFAULT)
  return errors
}

function year_validator(year) {
  const error_messages = []
  if (validator.isEmpty(year)) {
    error_messages.push("Empty string")
  }
  if (!validator.isInt(year, { min: 0, max: 99 })) {
    error_messages.push("must be number in [0, 99]")
  }
  return error_messages
}
