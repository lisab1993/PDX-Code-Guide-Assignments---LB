let textInput = document.querySelector('#text-input')
let textInputVal = textInput.value
let textArr = []
let counter = 0
let outputString = ''
let condArr = []

let settingsBtn = document.querySelector('#settings-btn')
let popup = document.querySelector('#popup')
let hdCol = document.querySelector('#hd-col')
let bgCol = document.querySelector('#bg-col')
let taCol = document.querySelector('#ta-col')
let fontCol = document.querySelector('#font-col')

let theHead = document.querySelector('#header')
let theBody = document.getElementsByTagName('body')[0]
let theArea = document.querySelector('#text-input')
let hdWrapper = document.querySelector('#hd-wrapper')
let bgWrapper = document.querySelector('#bg-wrapper')
let taWrapper = document.querySelector('#ta-wrapper')
let fontWrapper = document.querySelector('#font-wrapper')

let fontSizing = document.querySelector('#font-size')
let fontChoice = document.querySelector('#font-choice')
let fontArr = ['Arial', 'Arial Narrow', 'Arial Narrow Bold', 'Cambria', 'Coachin', 'Calibri', 'Courier New', 'Courier', 'Cursive', 'Fantasy', 'Franklin Gothic Medium', 'Geneva', 'Georgia', 'Gil Sans', 'Gil Sans MT', 'Haettenschweiler', 'Helvetica', 'Impact', 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Sans Unicode', 'Lucida Sans Grande', 'Monospace', 'Segoe UI', 'Serif', 'Trebuchet MS', 'Tahoma', 'Times New Roman', 'Times', 'Verdana']

// wrapper events
hdWrapper.addEventListener('input', (event) => {
    event.preventDefault()
    hdWrapper.style.backgroundColor = hdCol.value
})
bgWrapper.addEventListener('input', (event) => {
    event.preventDefault()
    bgWrapper.style.backgroundColor = bgCol.value
})
taWrapper.addEventListener('input', (event) => {
    event.preventDefault()
    taWrapper.style.backgroundColor = taCol.value
})
fontWrapper.addEventListener('input', (event) => {
    event.preventDefault()
    fontWrapper.style.backgroundColor = fontCol.value
})


// input type color events
bgCol.addEventListener('input', (event) => {
    //sets the far background via the color picker
    event.preventDefault()
    theBody.style.backgroundColor = bgCol.value
})

taCol.addEventListener('input', (event) => {
    //text area color from color picker
    event.preventDefault()
    theArea.style.backgroundColor = taCol.value
})

hdCol.addEventListener('input', (event) => {
    //header color
    event.preventDefault()
    theHead.style.backgroundColor = hdCol.value
})

// font styling events
fontCol.addEventListener('input', (event) => {
    //font color
    event.preventDefault()
    theArea.style.color = fontCol.value
})

fontSizing.addEventListener('input', (event) => {
    //font size
    event.preventDefault();
    theArea.style.fontSize = fontSizing.value + 'px'
})

fontChoice.addEventListener('click', (event) => {
    //font family (only the default fonts from vs code are used)
    event.preventDefault()
    theArea.style.fontFamily = fontChoice.value
})

// settings events
settingsBtn.addEventListener('mouseover', (event) => {
    //when the user hovers over the settings button, it goes dark
    event.preventDefault()
    settingsBtn.src = settingsBtn.src.replace('settings-light', 'settings-dark')
})

settingsBtn.addEventListener('mouseleave', (event) => {
    //when the user is no longer hovering over the settings button, it goes back to light
    event.preventDefault()
    settingsBtn.src = settingsBtn.src.replace('settings-dark', 'settings-light')
})

settingsBtn.addEventListener('click', (event) => {
    //open the settings panel
    event.preventDefault()
    let settings = window.getComputedStyle(popup)
    settings = settings.display
    if (settings === 'none') {
        popup.style.display = 'flex'
    } else {
        popup.style.display = 'none'
    }
})

// text input event
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

function getFonts() {
    //populate the drop down with font options
    //the default font families from vs code are used
    for (i in fontArr) {
        let option = document.createElement('option')
        option.innerText = fontArr[i]
        option.setAttribute('value', fontArr[i])
        option.style.fontFamily = fontArr[i]
        fontChoice.appendChild(option)
    }
}

function popFontSizes() {
    //populate the options in the font size drop down
    for (i = 7; i <= 48; i++) {
        let option = document.createElement('option')
        option.setAttribute('value', i)
        option.innerText = i
        fontSizing.appendChild(option)
    }
}

//override input functions
function finder(target, lower, upper) {
    //determines if a single number is between two numbers
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
            textArr.push(word += letter)
            word = ''
        }
    }
    //if there are several spaces next to each other, combine them into one string within the list; the argument is currently a whitespace, but anything can be passed in.
    //the condenser function will be used as the callback
    callback(' ')
}

// rbg to hex functions (3)
function getColor(element, property) {
    //give it an element and the css property you want to get(such as background-color, color, etc), and it'll get the rgb value as a list of numbers
    let startColor = (getComputedStyle(element).getPropertyValue(property))
    startColor = (startColor.slice(4, startColor.length - 1))

    startColor = startColor.split(', ')
    let outputArr = startColor.map(num => parseInt(num))
    return outputArr
}

function ColorToHex(color) {
    //converts a decimal number to hexadecimal for convertRGBtoHex
    var hexadecimal = color.toString(16);
    return hexadecimal.length == 1 ? "0" + hexadecimal : hexadecimal;
}

function convertRGBtoHex(array) {
    //turns a list of numbers into a hex code
    return "#" + ColorToHex(array[0]) + ColorToHex(array[1]) + ColorToHex(array[2]);
}


function loadup() {
    //runs as soon as the page is loaded
    //text from the html is grabbed for later use, and cleared so the user doesn't immediately see it
    textInput.innerHTML = ''

    //separator turns the desired output into a list of strings, and condensor keeps the whitespace from becoming repetetive
    separator(condensor)
    //populate the settings dropdown with font sizes and font family options. 
    getFonts()
    popFontSizes()

    //get the initial starting font size, and set it as the default for the select dropdown
    let startFontSize = window.getComputedStyle(theArea).getPropertyValue('font-size')
    startFontSize = startFontSize.slice(0, 2)
    fontSizing.value = startFontSize

    //set the visible wrapper default to the existing startup colors
    hdWrapper.style.backgroundColor = convertRGBtoHex(getColor(theHead, 'background-color'))
    bgWrapper.style.backgroundColor = convertRGBtoHex(getColor(theBody, 'background-color'))
    taWrapper.style.backgroundColor = convertRGBtoHex(getColor(theArea, 'background-color'))
    fontWrapper.style.backgroundColor = convertRGBtoHex(getColor(theArea, 'color'))
    
    //set the color pickers' default to the existing colors
    hdCol.value = convertRGBtoHex(getColor(theHead, 'background-color'))
    bgCol.value = convertRGBtoHex(getColor(theBody, 'background-color'))
    taCol.value = convertRGBtoHex(getColor(theArea, 'background-color'))
    fontCol.value = convertRGBtoHex(getColor(theArea, 'color'))
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