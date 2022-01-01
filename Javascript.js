'use strict';
console.log("Hello World");             // console log can print somthing on console

let firstName = "Lucifer MorningStar";  // var // Let // const
console.log(firstName);
let num = 42; console.log(num); console.log(num+4);

let name;       // let
name = 'Mark'; console.log(name);
name = 'Dennis'; console.log(name);
const name1  = 'Alo'; console.log(name1); // Const - Never change value
const PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132806647093844609550582231725359408128481117450284102701938;     //const
console.log(PI)

firstName = `Brenden`           // Var - not use anymore only for learning | VAriable can be Changed after assigned it
let lastName = 'Eich'
let fullName = `Mr.Sourav Biswas` // 
let age = 21
console.log('My Name is :',fullName);console.log(firstName.length);

let newstr = 'I am ' + firstName + ' and I am ' + age + ' years old';console.log(newstr);
newstr = `I am ${firstName} and I am ${age} years old`; console.log(newstr);
newstr = 'I \'am Sourav'; console.log(newstr);
newstr = '5926535897932384626433832795028841\n~S971693993751058209749445923078164062'; console.log(newstr);
newstr = firstName[3]; console.log(newstr);
let a = firstName.slice(1,-1); console.log(a);
console.log("Excel Your Habits");
newstr = firstName.substring(0,3);console.log(newstr);
newstr = firstName[5];console.log(newstr);
newstr  = firstName.toLowerCase();console.log(newstr);
newstr  = firstName.toUpperCase();console.log(newstr);

console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.MIN_SAFE_INTEGER);
console.log(2**53-1);
console.log(3*5/2%3);

console.log(2+3*4);
console.log((2+3));
console.log(2**1.5);

num = 1e3;console.log(num);
num = 1e-4;console.log(num);
num = 10_00_000;console.log(--num);
num = 3;num ++;console.log(num);

let num1 = 12.24; let num2 = "12"; console.log(num1 + num2);
let num3 = 12; let num4 = "10"; console.log(num3 - num4);
let num5 = parseFloat(num2);console.log(num1 + num5);

console.log(typeof num1); 
console.log(typeof num4); 
console.log(typeof num);

console.log(Math.round(num1));
console.log(Math.floor(num1));
console.log(Math.ceil(num1));
console.log(Math.log(num1));
console.log(Math.sqrt(num1));
console.log(Math.random(num1));

let random = Math.floor(Math.random()*100);
console.log(random)

let minNum = 100;let maxNum = 1010;
let random2 = Math.floor(Math.random()*(maxNum - minNum) + minNum);
console.log(random2)

let numb1 = 9007199254740991;
let numb2 = 9007199254740991;
console.log(numb1 * numb2)
console.log(1/0);

alert('Hallo World');
age = prompt('What is your age ?',25);
alert(`Hello, You're ${age} years old`);
console.log(typeof age);

let x = confirm('Are you sure ?');
console.log(x)

age = 4;
if(age>18){
    console.log('You are eligible for vote')
}else{
    console.log('You cannot be eligible for Vote')
}

let name2 = 'Bill Henry Gates';
if(name2){
    console.log(`Your Name is ${name2}`);
}else{
    console.log(`Please Enter your name!`);
}       // False Value = NaN, "", undefined,

                // Number Guessing Game
let winningNumber = 17;
num = parseInt(prompt("Enter a number : "));
if(num === winningNumber){
    console.log("You guessed it right, you win");
}else{
    if(num<winningNumber){
        console.log("too low !!!!");
    }else{
        console.log("too high !!!!");
    }
}

num = 24;
if(num>0){                       
    console.log("Number is Positive !!!!!!!");
}else if(num<0){
    console.log("Number is Negative !!!!!!!");
}else if(num === 0){
    console.log("Number is Zero !!!!!!!");
}else{
    console.log("Invalid Number");
}

let temp = 22;
if(temp<=-90){
    console.log("Hello Alien, What's your planet name ?");
}else if(temp<=0){
    console.log("It's Extremely cold outside");
}else if(temp<=10){
    console.log("It's very cold outside");
}else if(temp<=16){
    console.log("It's little cold outside");
}else if(temp<=25){
    console.log("It's perfectly fine wheather outside");
}else if(temp<=35){
    console.log("Lets go to swimming pool");
}else if(temp<=50){
    console.log("Please turn on the AC");
}else{
    console.log("What ????");
}

//              Function 
function sum3(num1, num2, num3){        //parameters
    return num1+num2+num3;
}

let total = sum3(96739,598787,9867);
console.log(total);         //arguments

function isEven2(num){
    if(num%2===0){
        return true;
    }
    return false;
}
console.log(isEven2(5));

function isEven3(num){
    return num%2===0;
}
console.log(isEven3(5));
console.log(4%2===0);

function greet(username){
    return `Hello, ${username}, Good Morning`
}
console.log(greet("Hamp"));

function singHapppyBirthday(){
    console.log("happy birthday to you");
    console.log("happy birthday to you");
    console.log("happy birthday dear .... ");
}
console.log(singHapppyBirthday());

// // Array
// // Create Array
let fruits = ['Apple', 'Mango', 'Grapes', 'Pear', 'Orange', 'Fig', 'Plum', 'Banana'];
let fruits2 = ['Pomegranate', 'Papaya', 'Peach'];
let fruits3 = ['Apricot', 'Coconut', 'Lychee'];
console.log(fruits);
console.log(fruits.length);

// Access Array Elements
console.log(fruits[5]);
// Update Array Elements
fruits[1] = 'Blueberries';
console.log(fruits);
// Push and Unshift
fruits.push('Blackberries', 'pineapple');
fruits.unshift('Lemon','Strawberries')
console.log(fruits);
// Pull and Shift
let poppedItem = fruits.pop();
console.log(poppedItem);
console.log(fruits);

let removeItem = fruits.shift();
console.log(removeItem);
console.log(fruits);

Splice
// remove
let deleteItems = fruits.splice(1,3);
console.log(fruits);
console.log(deleteItems);

// add
let addItems = fruits.splice(1,0,'Mulberries');
console.log(addItems);
console.log(fruits);

// Concat
let combine = fruits.concat(fruits2, fruits3);
console.log(combine);

// Slice
let sliceArray = fruits.slice(1, 3);
console.log(sliceArray);

// Include
console.log(fruits.includes('Fig',3));
console.log(fruits.includes('Orange',2));

// Index of
console.log(fruits.indexOf('Fig'));

// reverse
fruits.reverse();
console.log(fruits);

// Nested Array
let matrix = [[1,2,3], [4,5,6], [7,8,9]];
console.log(matrix);
console.log(matrix.length);

// Access Elements from Nested Array
console.log(matrix[2][1]);
console.log(matrix[1][2]);

//  Aore About Array
const myArray = ['items1', 'items2'];
myArray[0] = 'newItems';
console.log(myArray);

// For of Loop
for(let fruit of fruits){
    console.log(`Hello Mr. ${fruit}`);
}

// For in Loop
for(let fruit in fruits){
    console.log(`Hello Mr. ${fruits[fruit]}`);
    console.log(fruit);
}

// For Loop
for(let fruit = 0;fruit <fruits.length;fruit++){
    console.log(fruit);
}

// While Loop
let fruit = 0;
while(fruit<fruits.length){
    console.log(fruit);
    i++
}

// Date
let myDate = new Date();
console.log(myDate.getDate());
console.log(myDate.getMonth());
console.log(myDate.getFullYear());
console.log(myDate.getHours());
console.log(myDate.getMinutes());
console.log(myDate.getSeconds());
console.log(myDate.getDay());

// Object Oriented Programming in JavaScript
class Students{
    constructor(name,age,cls,roll){
        this.name = name;
        this.age = age;
        this.class = cls;
        this.roll = roll;
    }
    biodata(){
        console.log(`Hi I am ${this.name} I am ${this.age} years old and I am in class ${this.class} my roll no is ${this.roll}`);
    }
}

class Player extends Students{
    constructor(name,age,cls,roll,game){
        super(name,age,cls,roll)
        this.game = game;
    }
}

let obj1 = new Students('Sourav',24,'MCS',7);
obj1.biodata();

