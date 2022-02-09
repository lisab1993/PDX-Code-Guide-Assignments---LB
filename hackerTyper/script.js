let textInput = document.querySelector('#text-input')
let textInputVal = textInput.value
let textArr = []
let counter = 0
let outputString = ''
let condArr = []

function condensor(target) {
    let newLineCounter = 0
    for (i in textArr) {
        let word = textArr[i]
        if (word === target && textArr[i+1] === target){
            newLineCounter += 1
        } else if (word === target && textArr[i+1] !== target) {
            textArr.push(target.repeat(newLineCounter+1))
            newLineCounter = 0
        } else {
            condArr.push(word)
        }
    }
}


textInput.addEventListener('input', (event) => {
    //replace incoming text with hacker text from array
    event.preventDefault()
    if (counter != condArr.length){
        textInput.value = outputString += condArr[counter]
        counter += 1
    } else {
        counter = 0
    }


    // console.log(condArr)
    // for (i in condArr){
    //     for (j in condArr[i]) {
    //         console.log(condArr[i].charCodeAt(j))
    //     }
    // }
})


//ascii
//control characters: 0-31
//lowercase letters: 97-122
//uppercase letters: 65-90
//punctuations: 123-127; 91-96; 58-64; 32-47
//numbers: 48-57
//32 is a whitespace; 127 is delete
//10 is new line
//9 is tab



function finder(target, lower, upper) {
    //write a function to determine if a single number is between two numbers
    if (target >= lower && target <= upper) {
        return true
    } else {
        return false
    }
}



function separator(callback) {
    //turn the hacker code into a list of strings to be generated as typing happens
    let word = ""
    //loop through the hacker code
    //if the character is a letter (determined by its ascii code), the letter is added to the word string
    //if the character isn't a letter, add it to the word, push the word to the textApp, and clear the word to make another one
    for (i in textInputVal) {
        let letter = textInputVal[i]
        let textAscii = (textInputVal.charCodeAt(i))
        if (finder(textAscii, 97, 122)){
            word = word + letter
        } else if (finder(textAscii, 65, 90)){
            word = word + letter
        }else {
            // console.grou(letter, 'false')
            textArr.push(word += letter)
            word = ''
        }
    }
    callback(' ')
    // console.log(textArr, 'textArr')
}


function loadup() {
    //text from the html is grabbed for later use, and cleared so the user doesn't immediately see it
    textInput.innerHTML = ''

    //separator will use condensor as a callback function
    separator(condensor)
  }
