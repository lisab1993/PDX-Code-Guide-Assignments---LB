//title at top
//something saying to choose 
//three pictures with the options
//click on one to choose
//after clicking, the program will run
//the div output will have a picture for either victory or defeat, and will announce one or the other.

//connect to our html
let rock = document.querySelector("#rock")
let paper = document.querySelector("#paper")
let scissors = document.querySelector("#scissors")
let div_output = document.querySelector('#div_output')

// let selection = ''
//alternate way to write functions
rock.addEventListener("click", function() {
    let selection = 'rock'
    rps(selection)
})

paper.addEventListener("click", function(){
    let selection = 'paper'
    rps(selection)
})

scissors.addEventListener("click", function(){
    let selection = 'scissors'
    rps(selection)
})



const rps = function (selection) {
        let choices = ["rock", "paper", "scissors"]// an array of options for the computer to choose from.
        let computerChoice = Math.floor((Math.random() * 3) + 0)// select a random number between 0 and two. The selection is now attached to the computerChoice variable.
        computerChoice = choices[computerChoice] // the computerChoice variable will now use the random number as an index, and an option from the choices array will be held in this variable.
       
        // console.log(selection, computerChoice, "this is selection and computerChoice")

        //a switch also would work; look it up later. javascript switch case
        if (selection === computerChoice) { // look for a tie.
            div_output.innerText = "It is a tie"
        }

        // If it's a tie
        else if (selection === "rock" && computerChoice === "paper") {
            div_output.innerText =  "Paper covers rock. The computer wins."
        }
        else if (selection === "rock" && computerChoice === "scissors") {
            div_output.innerText =  "Rock smashes scissors. You win."
        }

        // If the user has paper
        else if (selection === "paper" && computerChoice === "scissors") {
            div_output.innerText =  "Scissors cuts paper. The computer wins."
        }
        else if (selection === "paper" && computerChoice === "rock") {
            div_output.innerText =  "Paper covers rock. You win."
        }

        // If the user has scissors
        else if (selection === "scissors" && computerChoice === "rock") {
            div_output.innerText =  "Rock smashes scissors. The computer wins."
        }
        else if (selection === "scissors" && computerChoice === "paper") {
            div_output.innerText =  "Scissors cuts paper. You win."
        }
}


