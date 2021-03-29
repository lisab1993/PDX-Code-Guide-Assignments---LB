

const fs = require('fs')
const path = require('path')

var file = process.argv[2]


fs.readdir(file, function callback(err, list) {
    if (err) {
        throw err
    } else {
        // var outputArray = []
        list.forEach(element => {
            if (path.extname(element) === "." + process.argv[3]) {
                console.log(element)
            }
        })
    }
})


