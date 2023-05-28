const questions = document.querySelectorAll('.question p')

questions.forEach((question_el)=>{
    question_el.onclick = (el) => {
        questions.forEach(q => {
            q.parentNode.parentNode.classList.remove('selected')
        })
        question_el.parentNode.parentNode.classList.add('selected')
    }
})

