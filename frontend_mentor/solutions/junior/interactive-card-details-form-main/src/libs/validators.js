import validator from "validator"

export {
  card_holder_validator,
  card_number_validator,
  cvc_validator,
  month_validator,
  year_validator,
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
