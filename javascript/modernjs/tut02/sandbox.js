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

// common string methods

result = email.lastIndexOf('n');
console.log(result);

result = email.slice(0, 8);
console.log(result);

result = email.substr(2, 8);
console.log(result);

// Replaces 1st occurrence
result = email.replace('domain', 'ninja');
console.log(result);


// Math
// Operators: +, -, *, /, **, %
let radius = 10;
const pi = 3.14;

console.log(radius, pi);

console.log(10/2);

// Modulus
result = radius % 3;
console.log(result);

result = pi * radius ** 2;
console.log(result);

// order of operation: BIDMAS
result = 5 * (10 - 3) ** 2;
console.log(result);

let likes = 10;
likes = likes + 1;
console.log(likes);

// Short hand
likes++;
console.log(likes);

likes += 1;
console.log(likes);

++likes;
console.log(likes);

console.log(++likes);

console.log(likes++);
console.log(likes);

// NaN - not a number

console.log(5 / 'hello');


// Concatenate numbers
result = 'the blog has ' + likes + ' likes';
console.log(result);

// template strings
const title = 'Best reads of 2019';
const author = 'Mario';


// concatenation way
result = 'The blog called ' + title + ' by ' + author + ' has ' + likes + ' likes';
console.log(result);

// template string way using back ticks
result = `The blog called ${title} by ${author} has ${likes} likes`;
console.log(result);

// creating html templates
let html = `
  <h2>${title}</h2>
  <p>By ${author}</p>
  <span>This blog has ${likes} likes</span>
`;
console.log(html);

// Arrays
let ninjas = ['shaun', 'ryu', 'chun-li'];
console.log(ninjas);

console.log(ninjas[1]);

ninjas[1] = 'ken';
console.log(ninjas[1]);

let ages = [20, 25, 30, 35];
console.log(ages[3]);

let random = ['ken', 20, 'ryu', 20];
console.log(random);

console.log(random.length);

// Array methods

// Joins all items separated by a command and returns a string.
result = ninjas.join(',');
console.log(result);

result = ninjas.indexOf('chun-li');
console.log(result);

result = ninjas.concat(['blanka', 'et']);
console.log(result);

// Pushes a new value into array and return new length
result = ninjas.push('it');
console.log(result);
console.log(ninjas);

result = ninjas.pop();
console.log(result);
console.log(ninjas);

// Undefined and null
let newAge;
console.log(newAge, newAge + 3, `the new age is ${newAge}`);

newAge = null;
console.log(newAge, newAge + 3, `the new age is ${newAge}`);

// booleans and comparisons
console.log(true, false);

// methods can return booleans
email = 'luigi@nintendo.com';

// returns boolean
result = email.includes('@');
console.log(result);

let names = ['mario', 'luigi', 'toad'];
result = names.includes('bowser');
console.log(result);

// comparison operators
console.log(age)
console.log(age == 25);
console.log(age == 30);
console.log(age != 30);

myName = 'eric';
console.log(myName);
console.log(myName == 'eric');
console.log(myName == 'Eric');  // Case sensitive
console.log(myName > 'eric');
console.log(myName > 'Eric');  // lowercase > uppercase
console.log(myName < 'Eric');

// loose comparison - different types can still be equal
console.log('25' == 25); // true

// strict comparison - different types cannot be equal
console.log('25' === 25); // false
console.log(25 === 25);
console.log('25' !== 25);
console.log(25 !== 25);

// type conversion
score = '100';
console.log(score + 1); // 1001
console.log(typeof score);

score = Number(score);
console.log(score + 1); // 101
console.log(typeof score);

result = String(10);
console.log(typeof result, result);

console.log(Boolean(0/'a'), Boolean(null), Boolean(0)); // false if NaN, null, or zero value.  Undefine throws exception
