const fs = require('fs');
var os = require('os');

fs.readFile('../input.txt', 'utf-8', (err, data) => {
    let count = 0
    let old = null
    if (err) {
        console.error(err)
        return
    }
    data = data.split(os.EOL)

    data.forEach(element => {
        element = parseInt(element)
        if (old == null) {
            old = element
        } else {
            if (element > old) {
                count = count + 1
            }
            old = element
        }
    })
    console.log("There are", count, "depth increases")
})
