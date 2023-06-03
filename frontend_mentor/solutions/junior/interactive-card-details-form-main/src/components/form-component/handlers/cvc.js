export { cvc_handler }

import validator from "validator"
import { on_validation } from "../../../libs/functions.js"
import { CVC_DEFAULT } from "../../../config.js"

function cvc_handler(element) {
  const cvc = element.input.value
  const errors = cvc_validator(cvc)
  on_validation(errors, element, cvc, CVC_DEFAULT)
  return errors
}

function cvc_validator(cvc) {
  const error_messages = []
  if (validator.isEmpty(cvc)) {
    error_messages.push("Empty string")
  }
  if (!validator.isInt(cvc)) {
    error_messages.push("must be number")
  }
  if (!validator.isLength(cvc, { min: 3, max: 3 })) {
    error_messages.push("length not equal 3")
  }
  return error_messages
}
