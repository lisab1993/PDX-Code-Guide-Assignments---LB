let add_task = document.querySelector("#add_task")// the field at the top where the user types the task.
let btn_add_task = document.querySelector("#btn_add_task")// the button that moves the task from the top input to the incomplete list.
let first_table_body = document.querySelector("#first_table_body")// the table body for unfinished tasks
let completed_table_body = document.querySelector("#completed_table_body")// the table body for finished tasks.

// Date does nothing, it's there to be pretty. 
// add_task gets the task from the user
// then the user clicks the add button
// when the button is clicked, the program will first take the value from the add_task.
// and pass it into a form with a checkbox or button. 





// This populates the first table - the one with incomplete tasks and a way to finish or delete them
btn_add_task.addEventListener("click", function (event) {
    // first_tr can be used several times to add different table datas.
    let first_tr = document.createElement("tr")// this will create a new row in the table

    //adding the task to the first table
    let task_td = document.createElement("td")// this creates a new td for the task
    task_td.innerText = add_task.value // the td will contain the text the user entered.
    first_tr.appendChild(task_td)// the td containing the task will be added to a new row in the table

    //making the done button
    let btn_done_td = document.createElement("td")// creates a table data slot for our done button
    let span_done_button = document.createElement("span")//creates a span, which is like a div, but smaller and in-line. 
    span_done_button.innerText = "Done"// the button will say done
    span_done_button.classList.add("btn", "btn-primary")//the span will have a button using bootstrap formatting for the blue primary button
    btn_done_td.appendChild(span_done_button)//add the done button to the table data
    first_tr.appendChild(btn_done_td)//add the table data with the button to the row

    //add all the new rows to the table body
    first_table_body.appendChild(first_tr)// the row with the data will be added to the first tbody.


    //the second table - where completed tasks go, but can still be deleted
    span_done_button.addEventListener("click", function (event) {
        //completed_tr will create new table rows for the second table
        let completed_tr = document.createElement("tr")

        //adding the task to the second table
        let finished_task_td = document.createElement("td")// a td for the finished task
        finished_task_td.innerText = task_td.innerText//the td with the text is taken from the first table and passed into the second table

        completed_tr.appendChild(finished_task_td)// the task will be added to a new table row
        completed_table_body.appendChild(completed_tr)// all rows are added to the second tbody
    })

})




