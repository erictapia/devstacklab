// Nodejs - global object

// Outputs all attributes and methods in the global object
console.log(global)

// Sets a timeout to run after 3 seconds, outputs string and clears the interval
global.setTimeout(() => {
    console.log('in the timeout');
    clearInterval(interval);   
}, 3000);

// Sets the interval and runs every second
const interval = setInterval(() => {
    console.log('in the interval');
}, 1000);

// Fullpath of current script without filename
console.log(__dirname);

// Fullpath and filename of the script
console.log(__filename);
