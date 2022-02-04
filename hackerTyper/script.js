let textInput = document.querySelector('#text-input')
let textInputVal = textInput.value
let test = document.querySelector('#test')

let output = 'Lorem ipsum jfdkslfjnsda jkfldsjfkdsla jfkdslfjdskla jkfldsjal'
textInput.addEventListener('input', (event) => {
    event.preventDefault()
    
})

//when input comes in, don't let the original char in textarea
//replace it with some of the desired output text