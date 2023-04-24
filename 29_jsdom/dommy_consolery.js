

// Team Phantom Tollbooth :: Aaron Gershkovich, Sebastian Ching
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-019=
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//type in f(x) and you will get x +30


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
   // type in "o" and you will get everything in the brackets      


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
// Just adds a word in a new row.


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
// Just removes item that it specified, but will keep removing the next one if you execute the same function again.


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};
//Makes the first and last lines red?


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
//Makes the first line red?

//insert your implementations here for...
// FIB
// FAC
// GCD


var fib = function(n) {
if (n < 2) {
    return n;
  }
  return fib(n-1) + fib(n-2);
}

var fac = function(n){
  if (n === 0) {
    return 1;
  }
  return n * fac(n-1);
}

var gcd = function(a,b){
 if (b===0) {
  return a;
  }
  return gcd (b, a % b);
}

var button = document.getElementById("myBtn"); 
button.addEventListener("click", callfib);  
function callfib(){
var addfib = document.getElementById("fibn").value;
console.log(fib(addfib));
}

var button = document.getElementById("Fac"); 
button.addEventListener("click", callfac);  
function callfac(){
var addfac = document.getElementById("fibn").value;
console.log(fac(addfac));
}

var button = document.getElementById("Gcd"); 
button.addEventListener("click", callGcd);  
function callGcd(){
var addGcd = document.getElementById("fibn").value;
var addGcd2 = document.getElementById("fib2").value;
console.log(gcd(addGcd, addGcd2));
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

