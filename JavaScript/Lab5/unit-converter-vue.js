//input field for starting units
//input field for ending units
//input field for distance
//button to get the distance
//output field for the final answer.


let app = new Vue({
    el: "#app",
    data: {
        //these 4 are connected to our v-model, and they make up our input/output
        input_starting_units: "feet",
        input_ending_units: "feet",
        input_distance: "",
        output: "",
    },
    methods: {
        calculate: function () {
            let to_meters = {//convert user's distance in starting units to meters.
                "feet": 0.3048,
                "miles": 1609.344,
                "meters": 1.0,
                "kilometers": 1000.0,
                "yards": 0.9144,
                "inches": 0.0254,
            }

            let from_meters = {//convert the user's distance from meters to requested units.
                "feet": 3.28,
                "miles": 0.000621371,
                "meters": 1,
                "kilometers": 0.001,
                "yards": 1.09361,
                "inches": 39.3701,
            }
            // Conversions
            // console.log(this.input_starting_units, this.input_ending_units, this.input_distance)
            let in_meters = this.input_distance * to_meters[this.input_starting_units]//convert to meters
            let final_distance = in_meters * from_meters[this.input_ending_units] //convert to the desired units. 
            let final_distance_rounded = final_distance.toFixed(1)//this rounds to the nearest tenth
            this.output = this.input_distance + " " + this.input_starting_units + " is " + final_distance_rounded + " " + this.input_ending_units
        }
    }
})
