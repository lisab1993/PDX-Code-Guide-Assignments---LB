const addTask = document.querySelector('#addTask')
const btnAddTask = document.querySelector('#btnAddTask ')
const IncTableBody = document.querySelector('#IncTableBody')
const comTableBody = document.querySelector('#comTableBody')

    //local storage
    const itemsArray = []


btnAddTask.addEventListener("click", ((event) => {
    //table row and table data to add tasks
    const incTableRow = document.createElement('tr')
    const incTableData= document.createElement('td')
    //the table data's text will be the user input
    incTableData.innerText = addTask.value
    //which is then added to the table row
    incTableRow.appendChild(incTableData)


    //a table data spot for the done button
    const doneBtnTD = document.createElement('td')
    //done button will be made from a span
    const doneBtnSpan = document.createElement('span')

    //Set the text and class for the done button
    doneBtnSpan.innerText = 'Done'
    doneBtnSpan.classList.add('btn', 'btn-primary')

    //the span/button is added to its table data slot, then to the table row 
    doneBtnTD.appendChild(doneBtnSpan)
    incTableRow.appendChild(doneBtnTD)
    IncTableBody.appendChild(incTableRow)
    addTask.value = ''

    //delete button
    const deleteBtnTD = document.createElement('td')
    const deleteBtnSpan = document.createElement('span')
    deleteBtnSpan.innerText = 'Delete'
    deleteBtnSpan.classList.add('btn', 'btn-danger')
    deleteBtnTD.appendChild(deleteBtnSpan)
    incTableRow.appendChild(deleteBtnTD)
    IncTableBody.appendChild(incTableRow)

    //saving to local storage
    localStorage.setItem('tasks', JSON.stringify(itemsArray))
    const data = JSON.parse(localStorage.getItem('tasks'))

    //done button function
    doneBtnSpan.addEventListener('click', ((event) => {
        const completeTableRow = document.createElement('tr')
        const completeTableData = document.createElement('td')
        completeTableData.innerText = incTableData.innerText
        completeTableData.classList.add('complete-task')
        completeTableRow.appendChild(completeTableData)
        comTableBody.appendChild(completeTableRow)
        incTableRow.parentNode.removeChild(incTableRow)
    
    }))

    //delete button function
    deleteBtnSpan.addEventListener('click', ((event) => {
        incTableRow.parentNode.removeChild(incTableRow)
    }))
}))

