// 4 different strings with the pieces to make a password
console.log("Hello World")
let lower = "abcdefghijklmnopqrstuvwxyz"
let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let punctuation = "!@#$%^&*?"
let nums = "0123456789"

let possibilities = lower + upper + punctuation + nums // concatenate the strings above into a single variable.


function generator(password_length) {
    let i = 0
    let password = ""// our password is a blank string that we will add on to. It's outside the loop so that a new one doesn't generate each time.
    while (i < password_length) {
        let randomIndexSelector = Math.floor(Math.random() * possibilities.length) // This will give us a number. That number will grab a random option from possibilities by its index.
        let randomCharacter = possibilities.charAt(randomIndexSelector)// randomCharacter will now reach into the possibilities string, and pull out the character at our random index.
        password += randomCharacter// Add the random character to the password string. Do this until the password is at the correct length.
        i++
    }
    return password
}

// console.log(generator(12))

let input_password_length = document.querySelector('#input_password_length')
let btn_get_password = document.querySelector('#btn_get_password')
let div_output = document.querySelector('#div_output')

// btn_say_hello.onclick = function() {}
btn_get_password.addEventListener('click', function() {
    let output = generator(input_password_length.value)
    div_output.innerText = output
    
})

