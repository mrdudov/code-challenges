export { on_validation, has_no_errors, by_four }

function on_validation(error_list, element, value, default_value) {
  if (error_list.length !== 0) {
    element.error.classList.remove("hidden")
    element.error.innerHTML = error_list[0]
    element.output.innerHTML = default_value
  } else {
    element.error.classList.add("hidden")
    element.output.innerHTML = value
  }
}

function has_no_errors(errors) {
  let all_errors = []
  for (let error of errors) {
    all_errors = all_errors.concat(error)
  }
  return all_errors.length === 0
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
