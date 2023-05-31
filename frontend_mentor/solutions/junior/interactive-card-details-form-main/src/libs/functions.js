export { on_validation }

function on_validation(error_list, element) {
  if (error_list.length !== 0) {
    element.classList.remove("hidden")
    element.innerHTML = error_list[0]
  } else {
    element.classList.add("hidden")
  }
}
