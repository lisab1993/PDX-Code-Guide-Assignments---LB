

while (true) {
    let choices = ["rock", "paper", "scissors"]// an array of options for the computer to choose from.
    let computerChoice = Math.floor((Math.random() * 3) + 0)// select a random number between 0 and two. The selection is now attached to the computerChoice variable.
    computerChoice = (choices[computerChoice]) // the computerChoice variable will now use the random number as an index, and an option from the choices array will be held in this variable.

    alert("Welcome to rock paper scissors!")// welcome screen
    let playGame = prompt("Would you like to play rock, paper, scissors against the computer? Please enter yes or no:")// ask the user if they want to play; this will be used in our REPL.



    if (playGame === "yes") {// see if the user wants to play. When they say "no", the REPL will break. Most of the game will be within these curly brackets because it will all run if the user says "yes".
        let userInput = prompt("Please select either rock, paper, or scissors: ")// the user's choice is now stored within userInput

        if (userInput === computerChoice) {// look for a tie.
            alert("It's a tie!!!")
        }

        // If the user has rock
        else if (userInput === "rock" && computerChoice === "paper") {
            alert("Paper covers rock. The computer wins!")
        }
        else if (userInput === "rock" && computerChoice === "scissors") {
            alert("Rock smashes scissors. You win!")
        }

        // If the user has paper
        else if (userInput === "paper" && computerChoice === "scissors") {
            alert("Scissors cuts paper. The computer wins!")
        }
        else if (userInput === "paper" && computerChoice === "rock") {
            alert("Paper covers rock. You win!")
        }

        // If the user has scissors
        else if (userInput === "scissors" && computerChoice === "rock") {
            alert("Rock smashes scissors. The computer wins!")
        }
        else if (userInput === "scissors" && computerChoice === "paper") {
            alert("Scissors cuts paper. You win!")
        }
    }
    else {// If the user writes anything other than "yes" when asked if they want to play, we'll say goodbye to them. 
        alert("Goodbye")
        break// This will break the loop after one of the comparison statements runs.
    }
}
