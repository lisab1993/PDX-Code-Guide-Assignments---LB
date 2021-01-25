/*
 * when you click a number button, the calculate function is ran with your option as the first number.
 */

let app = new Vue({
    el: "#app",
    data: {
        first_number: "",
        operator: "",
        second_number: "",
        output: "",
        visible_output: "",
        holding: "",

    },
    methods: {
        calculator: function (calc_num) {
            this.visible_output += calc_num
            this.holding += calc_num
            console.log(this.holding)
        }, math_operator: function (operation) {
            this.visible_output += operation
            this.first_number = this.holding
            this.holding = ""
            this.operator = operation
            console.log(this.output)
        }, equals: function () {
            this.second_number = this.holding
            if (this.operator === "+") {
                this.output = parseFloat(this.first_number) + parseFloat(this.second_number)
            } else if (this.operator === "-") {
                this.output = parseFloat(this.first_number) - parseFloat(this.second_number)
            } else if (this.operator === "*") {
                this.output = parseFloat(this.first_number) * parseFloat(this.second_number)
            } else if (this.operator === "/") {
                this.output = parseFloat(this.first_number) / parseFloat(this.second_number)
            } else if (this.operator === "^") {
                let carat_hold = this.first_number //the local variable will copy the first number 
                for (let i=1; i < this.second_number; ++i) {// we will keep run the loop the same number of times as our second number 
                    carat_hold = carat_hold * this.first_number// carat_hold will accumulate the total, and this.first_number will do the multiplication to add to it.
                }
                this.output = carat_hold
            }
        }, backspace: function () {
            this.holding = this.holding.substring(0, this.holding.length - 1)
            this.visible_output = this.visible_output.substring(0, this.visible_output.length - 1)
        }
    }
})



/*

starting state
output = ''
first_number = ''
operator = ''
second_number = ''

=============

user hits '3'
output = '3'

user hits '5'
output = '35'

user hits '8'
output = '358'


user hits '+'
first_number = output
operator = '+'
output = ''


user hits '2'
output = '2'

user hits '7'
output '27'

user hits '='
second_number = output
output = ''


=============

sending state
first_number = '358'
operator = '+'
second_number = '27'

parse first_number and second_number as floats
use conditionals to figure out what operator you have
do the calculation, store the result in output

*/




//when they hit the operator, store the current output as first num and reset the output to a blank string
//and store the operator
//pass the operator to a function

//when the user hits the equals sign, so take the current output and store it as second number.
//output is accumulating