export { on_validation, has_no_errors }

function on_validation(error_list, error_element, output_element, value) {
  if (error_list.length !== 0) {
    error_element.classList.remove("hidden")
    error_element.innerHTML = error_list[0]
    output_element.innerHTML = ""
  } else {
    error_element.classList.add("hidden")
    output_element.innerHTML = value
  }
}

function has_no_errors(errors) {
  let all_errors = []
  for (let error of errors) {
    all_errors = all_errors.concat(error)
  }
  return all_errors.length === 0
}
