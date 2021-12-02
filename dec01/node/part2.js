const fs = require('fs');
var os = require('os');

fs.readFile('../input.txt', 'utf-8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    let count = 0
    let index = 0

    data = data.split(os.EOL)

    let a = 0
    let b = 0
    let c = 0
    let d = 0

    while (index + 3 < data.length) {
        a = parseInt(data[index])
        b = parseInt(data[index + 1])
        c = parseInt(data[index + 2])
        d = parseInt(data[index + 3])
        if ((a+b+c) < (b+c+d)) {
            count++
        }
        console.log("Processed", d, "at index", index)
        index++
    }

    console.log("There are", count, "depth increases across 3 element ranges.")
})
