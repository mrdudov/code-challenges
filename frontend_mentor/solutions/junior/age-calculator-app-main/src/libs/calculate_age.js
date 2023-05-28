export { calculate_age } 


function calculate_age(date) {
    const birth_date = new Date(date['year'], date['month'] - 1, date['day'])
    const delta = new Date(Date.now() - birth_date)

    return {
        'year': delta.getFullYear() - 1970,
        'month': delta.getMonth(),
        'day': delta.getDate()
    }
}
