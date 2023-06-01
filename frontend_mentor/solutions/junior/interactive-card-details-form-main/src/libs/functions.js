export { on_validation, by_four }

function on_validation(error_list, error_element, output_element, value) {
  if (error_list.length !== 0) {
    error_element.classList.remove("hidden")
    error_element.innerHTML = error_list[0]
    output_element.innerHTML = ''
  } else {
    error_element.classList.add("hidden")
    output_element.innerHTML = value
  }
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
