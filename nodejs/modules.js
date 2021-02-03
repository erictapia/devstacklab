// xyz has both variables, people and ages
const xyz = require('./people');

// ages only has ages in people
const { ages } = require('./people')

// No ability to use objects from a required file
// unless the required file declares a module export
console.log(xyz)

// Individual access
console.log(xyz.people)

// Ages
console.log(ages)

// Builtin Nodejs
const os = require('os');
console.log(os);

console.log(os.platform(), os.homedir());