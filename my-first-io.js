
const fs = require('fs')

let data = fs.readFileSync(process.argv[2])
let output = data.toString().split('\n').length - 1

console.log(output)