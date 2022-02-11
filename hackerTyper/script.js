let textInput = document.querySelector('#text-input')
let textInputVal = textInput.value
let textArr = []
let counter = 0
let outputString = ''
let condArr = []

let settingsBtn = document.querySelector('#settings-btn')
let popup = document.querySelector('#popup')
let bgCol = document.querySelector('#bg-col')
let taCol = document.querySelector('#ta-col')
let fontCol = document.querySelector('#font-col')

let theBody = document.getElementsByTagName('BODY')[0]
let theArea = document.querySelector('#text-input')

let fontSize = document.querySelector('#font-size')



bgCol.addEventListener('input', (event) => {
    event.preventDefault()
    theBody.style.backgroundColor = bgCol.value
    console.log(bgCol.value, 'bg color')
})

taCol.addEventListener('input', (event) => {
    event.preventDefault()
    theArea.style.backgroundColor = taCol.value
    console.log(taCol.value, 'ta color')
})

fontCol.addEventListener('input', (event) => {
    event.preventDefault()
    theArea.style.color = fontCol.value
    console.log(fontCol.value, 'font color')
})



settingsBtn.addEventListener('click', (event) => {
    event.preventDefault()
    let settings = window.getComputedStyle(popup)
    settings = settings.display
    if (settings === 'none') {
        popup.style.display = 'flex'
    } else {
        popup.style.display = 'none'
    }
})

textInput.addEventListener('input', (event) => {
    //replace incoming text with hacker text from array
    event.preventDefault()
    if (counter != condArr.length) {
        textInput.value = outputString += condArr[counter]
        counter += 1
    } else {
        counter = 0
    }
})


function finder(target, lower, upper) {
    //write a function to determine if a single number is between two numbers
    if (target >= lower && target <= upper) {
        return true
    } else {
        return false
    }
}

function condensor(target) {
    let newLineCounter = 0
    for (i in textArr) {
        let word = textArr[i]
        if (word === target && textArr[i + 1] === target) {
            newLineCounter += 1
        } else if (word === target && textArr[i + 1] !== target) {
            textArr.push(target.repeat(newLineCounter + 1))
            newLineCounter = 0
        } else {
            condArr.push(word)
        }
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
        if (finder(textAscii, 97, 122)) {
            word = word + letter
        } else if (finder(textAscii, 65, 90)) {
            word = word + letter
        } else {
            // console.grou(letter, 'false')
            textArr.push(word += letter)
            word = ''
        }
    }
    //if there are several spaces next to each other, combine them into one string within the list; the argument is currently a whitespace, but anything can be passed in.
    callback(' ')
}


fontSize.addEventListener('input', (event) => {
    event.preventDefault()
    console.log('change')
})



function getColor(element) {
    //give it an element, and it'll get the rgb value as a list of numbers
    let startColor = (getComputedStyle(element).getPropertyValue('background-color'))
    startColor = (startColor.slice(4, startColor.length - 1))

    startColor = startColor.split(', ')
    let outputArr = startColor.map(num => parseInt(num))
    return outputArr
}


function ColorToHex(color) {
    var hexadecimal = color.toString(16);
    return hexadecimal.length == 1 ? "0" + hexadecimal : hexadecimal;
}

function ConvertRGBtoHex(array) {
    //turns a list of numbers into a hex code

    return "#" + ColorToHex(array[0]) + ColorToHex(array[1]) + ColorToHex(array[2]);
}


function loadup() {
    //text from the html is grabbed for later use, and cleared so the user doesn't immediately see it
    textInput.innerHTML = ''

    //separator will use condensor as a callback function
    separator(condensor)

    //populate the options in the font size drop down
    for (i = 7; i <= 48; i++) {
        let option = document.createElement('option')
        option.setAttribute('value', i)
        option.innerText = i
        fontSize.appendChild(option)
    }

    bgCol.value = ConvertRGBtoHex(getColor(theBody))
    taCol.value = ConvertRGBtoHex(getColor(theArea))
    // fontCol.value = ConvertRGBtoHex(getColor())
}


//ascii
//control characters: 0-31
//lowercase letters: 97-122
//uppercase letters: 65-90
//punctuations: 123-127; 91-96; 58-64; 32-47
//numbers: 48-57
//32 is a whitespace; 127 is delete
//10 is new line
//9 is tab