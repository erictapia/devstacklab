// Shows an alert message box
alert("hello, world");

// This can be seen on browser's development console tab
console.log(1);

// Assigning variable using the let keyword
let age = 25;
let year = 2019;

// Can log multiple variables by separating by a comma
console.log(age, year);

// Once a variable is defined, variable can be assigned other values
age = 30;
console.log(age);

// Defining a constant variable, it cannot be changed
const points = 100;

// Trying to assign a value to a constant variable will produce a:
// Uncaught TypeError: Assignment to constant variable
//points = 50;

console.log(points);

// var is an old keyword used for creating variables
var score = 75;
console.log(score);

/*
Variable name
  - cannot start with a number
  - can use letters, numbers, and $
*/
let $name = 1;
let name$ = 2;
console.log($name, name$);

// ********************* DATA TYPES

// strings
console.log('hello, world');

let email = 'et@domain.com';
console.log(email);

// string concatenation
let firstName = 'Eric';
let lastName = "Tapia";
let fullName = firstName + ' ' + lastName;
console.log(fullName);

// getting a character
console.log(fullName[0]);

// getting string length
console.log(fullName.length);

// string methods
console.log(fullName.toUpperCase());

let result = fullName.toLowerCase();
console.log(result);

let index = email.indexOf('@');
console.log(index);