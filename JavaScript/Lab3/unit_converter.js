let input_starting_units = document.querySelector('#input_starting_units')
let input_ending_units = document.querySelector('#input_ending_units')
let input_distance = document.querySelector('#input_distance')
let btn_go = document.querySelector('#btn_go')
let div_output = document.querySelector('#div_output')




function conversion(starting_units, ending_units, distance) {
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
    let in_meters = distance * to_meters[starting_units]//convert to meters
    let target_number = in_meters * from_meters[ending_units]//convert to the desired units. 
    return target_number
}



btn_go.addEventListener('click', function () {
    let output = conversion(input_starting_units.value, input_ending_units.value, input_distance.value)
    div_output.innerText = output
})
