// Variables and operators https://www.theodinproject.com/lessons/foundations-variables-and-operators

/* variables declarations
let name = 'john';
let age = 25;
let birthday = 'july 22 of 1995';

 that is an easy to read way to declare your variables, but there are other ways like:

let name = 'john';
    age = 25;
    birthday = 'july 22 of 1995';

Summary

We can declare variables to store data by using the var, let, or const keywords.

    let – is a modern variable declaration.
    var – is an old-school variable declaration. Normally we don’t use it at all,
    but we’ll cover subtle differences from let in the chapter The old "var", just in case you need them.
    const – is like let, but the value of the variable can’t be changed.

Tasks
Working with variables
- Declare two variables: admin and name.
- Assign the value "John" to name.
- Copy the value from name to admin.
- Show the value of admin using alert (must output "john").

let admin;
    name;
name = 'john';
admin = name;
alert(admin);

Giving the right name
- Create a variable with the name of our planet. How would you name such a variable?
- Create a variable to store the name of a current visitor to a website. How would you name that variable?
let ourPlanetName = "Earth";
let currentUserName;

Uppercase const?
Would it be right to use upper case for birthday? For age? Or even for both?
const BIRTHDAY = '18.04.1982'; // make birthday uppercase?
const AGE = someCode(BIRTHDAY); // make age uppercase?
uppercase is only right to use in the birthday variable because the value is already known before the execution

Basic operators .. javascript.info

String concatenation with binary +
usually the plus operator + sums numbers.
But, if the binary + is applied to strings, it merges (concatenates) them:

let s = "my" + "string";
alert(s); // mystring
alert( '1' + 2 ); // "12"
alert( 2 + 2 + '1' ); // '41' and not '221'

the binary + is the only opetors that supports strings in such a way. Other arithmetic operators work only with
numbers and always convert their operands to numbers
here's the demo for substraction and division:
alert( 6 - '2' ); // 4, converts '2' to a number
alert( '6' / '2' ); // 3, converts both operands to numbers

TASKS
The postfix and prefix forms
What are the final values of all variables a, b, c, and d after the code below?
let a = 1, b = 1;

let c = ++a; // ? i think this would return 2
let d = b++; // ? and this would return 1

alert(a)   // returns 2
alert(b)   // returns 2

Assignment result
What are the values of a and x after the code below?

let a = 2;

let x = 1 + (a *= 2);

alert(a);  // returns 4
alert(x);  // returns 5

Type conversions
What are results of these expressions?

"" + 1 + 0		// "10"
"" - 1 + 0		// "-1"
true + false	// "true or 1"
6 / "3"		    // "2"
"2" * "3"		// "6"
4 + 5 + "px"	// "9px"
"$" + 4 + 5		// "$45"
"4" - 2		    // "2"
"4px" - 2		// "2px?" ERROR this returns NaN
"  -9  " + 5	// "  -9  5"
"  -9  " - 5	// "-14"
null + 1		// "1?" (1)
undefined + 1	// "1?" ERROR this returns NaN (2)
" \t \n" - 2	// "-2" (3)

1. null becomes 0 after the numeric conversion.
2. undefined becomes NaN after the numeric conversion.
3. Space characters are trimmed off string start and end
when a string is converted to a number. Here the whole string
consists of space characters, such as \t, \n and a "regular" space
between them. So, similarly to an empty string, it becomes 0.

# Comparison tasks from Javascript.info
tasks
comparisons
what will be the result for these expressions?
5 > 4                    //true
"apple" > "pineapple"    //false
"2" > "12"               //true?
undefined == null        //true
undefined === null       //false
null == "\n0\n"          //false?
null === +"\n0\n"        //false
some of the reasons:
1. Obviously,true.
2. Dictionary comparison, hence false. "a" is smaller than "p".
3. Again, dictionary comparison, first char "2" is greater than the first char "1".
4. Values =null= and =undefined= equal each other only.
5. Strict equality is strict. Different types from both sides lead to false.
6. Similar to =(4)=, =null= only equals =undefined=.
7. Strict equality of different types.

Logical Operators javascript.info
Tasks
What's the result of OR?
what is the code below output?
alert( null || 2 || undefined ); // this would return "2" cause or always looks for the first truthry value

What's the resu of OR'ed alerts?
What will the code below output?
alert( alert(1) || 2 || alert(3) ); // i think this would return 1? or maybe 2. I'm not sure.

What is the result of AND?
What is this code going to show?
alert( 1 && null && 2 ); // is going to return "null" same logic as or but with the "falsy" values.

What is the result of AND'ed alerts?
What will this code show?
alert( alert(1) && alert(2) ); // if there are not falsy values returns the last one "2"

The resu of OR AND OR
What will the result be?
alert( null || 2 && 3 || 4 ); // 3 or 4?

Check the range outside
Write an if condition to check tat age is NOT between 14 an 90 inclusively.
Create two variants: the first one using NOT !, the second one - without it.

function withNOTOperator(age) {

    if(age != 14 %% age <= 13 && age >= 91 &&  age != 90) {
        alert( `your age is valid ${age}`)
 }
}
BAD, this doesn't work it's much simpler than that. here it is:
if (!(age >= 14 && age <= 90))return 'haha';

function withoutNOTOperator(age) {
    if (age <= 14) {
        alert( "you can enter the room" );
    }
    if (age >= 90)alert( " you can enter the room" );
}
this one is okey, tho i can be more simpler like if (age < 14 || age > 90)return 'lol';

A question about "if"
Which of these alerts are going to execute?
What will the results of the expressions be inside if(...)?
if (-1 || 0) alert( 'first' );          // doesn't reach alert? Maybe it reaches
if (-1 && 0) alert( 'second' );         // doesn't reach alert
if (null || -1 && 1) alert( 'third' );  // doesn't reach?
Executes
Operator && has a higher precedence than ||
so -1 && 1 executes first, giving us the chain:
null || -1 && 1  ->  null || 1  ->  1

Check the login

Write the code which asks for a login with prompt.

If the visitor enters "Admin", then prompt for a password, if the input is an empty line or Esc – show “Canceled”, if it’s another string – then show “I don’t know you”.

The password is checked as follows:

    If it equals “TheMaster”, then show “Welcome!”,
    Another string – show “Wrong password”,
    For an empty string or cancelled input, show “Canceled”

function login() {
    let user = prompt("user")

    if (user == "" || user == null) {
    alert ("Canceled");
    } else if (user != "Admin") {
    alert ("I don’t know you");
    } else if (user == "Admin") {
        let pass= prompt( "password")
        if (pass == "" || "pssword" == null) {
        alert ("canceled");
        } else if(pass != "TheMaster") {
        alert ("Wrong password");
        } else if(pass == "TheMaster") {
        alert ("Welcome!");
        }
    }
}
*/
/*
if else javascript.info
Tasks
If (a string with zero)
will =alert= be shown?
*/

if ("0") {
    alert("hello");
}
// yes alert is returned because not empty string becomes =true= values.

/*
The name of JavaScript
Using the =if..else construct, write the code which asks:'What is the "oficial" name of JavaScript?'

If the visitor enters "ECMAScript", then output "Right!", otherwhise -- output: "You don't know? ECMAScript!";
*/

function nameOfJavasSript() {
    let name = prompt('What\'s the "official" name of JavaScript?', '')
    if (name === "ECMAScript") {
        alert("Right!");
    } else {
        alert("You don't know? ECMAScript!");
    }
}

/*
 * Show the sign
 * Using =if...else=, write the code which gets a number via =prompt= and then shows in =alert=:
 * - =1=, if the value is greater than zero,
 * - =-1=, if less than zero,
 * - =0=, if equals zero.
 * In this task we assume that the input is always a number.
 */

function numberTypeDetection() {
    let number = prompt("insert a number")

    if (number > 1) {
        alert(1);
    } else if (number < 0) {
        alert(-1);
    } else {
        alert(0);
    }
}

/*
 * Rewrite 'if' into '?'
 * Rewrite this =if= usng the conditional operator '?':
 * let result;
*
* if (a + b < 4 ) {
*   result = 'Below';
* } else {
 *  result = 'over';
 *  }
 */

let result = (a + b < 4) ? result = 'Below' : result = 'Over';

/*
 * Rewrite 'if...else' into '?'
 * Rewrite =if...else= using multiple ternary operators '?'.
 * For readability, it's recommended to split the code into multiple lines.
 *
 * let message;
* if (login == 'Employee') {
*   mesage = 'Hello';
* } else if (login == 'Director') {
*   message = 'Greetings';
* } else if (login == '') {
*   message = 'no login';
* } else {
*   message = '';
* }
*/

let message = (login == 'Employee') ? 'Hello'
    : (login == 'Director') ? 'Greetings'
        : (login == '') ? 'no login'
            : '';

/*
 * switch javascript.info
 * Rewrite the "switch" into an "if"
 * Write the code using =if...else= which would correspond to the following =switch=:
 *
 * switch (browser) {
 *  case 'Edge':
 *      alert( "You've got the Edge!" );
*      break;
*   case 'Chrome':
*   case 'Firefox':
*   case 'Safari':
*   case 'Opera':
*       alert( "Okay we support these browsers too" );
*       break;
*   default:
*       alert( "We hope that this page looks ok!" );
 * }
 */

function browserSupport(browser) {
    if (browser === "Edge") {
        alert("You've got the Edge!");
    } else if (browser === "Chrome"
        || browser === "Firefox"
        || browser === "Safari"
        || browser === "Opera") {
        alert("Okay we support the browsers too");
    } else {
        alert("We hope that this page looks ok!");
    }
}

// Please NOTE: the constructor =browser == 'Chrome' || browser == 'Firefox' ...= is split into
// multiple lines for better readability.
// But the =switch= construct is still cleaner and more descriptive.

/*
 * Rewrite "if" into "switch"
 * Rewrite the code below using  single =switch= statement:
 *
 * let a = +prompt('a?', '');
*
* if (a == 0) {
*   alert( 0 );
* }
* if (a == 1) {
*   alert( 1 );
* }
* if (a == 2 || a == 3) {
*   alert( '2,3' );
* }
*/

function numbers() {
    let a = +prompt('a?', '');

    switch (a) {
        case 0:
            alert(0);
            break;
        case 1:
            alert(1);
            break;
        case 2:
        case 3:
            alert('2,3');
            break;
    }
}
// Please NOTE: the =break= at the bottom is not required. But we put it to make the code future-proof.
// In the future, there is a chance that we'd want to add one more =case=, for example =case 4=. And if we
// forget to add  break before it, at the end of =case 3=, there willbe an error. So that's a kind of self-
// insurance.

/*
 * Foundations data types and conditionals Assignment
 * Exercise 1
/**
 * ===== Troubleshooting =====
 * The function below should log the number 2, however it does not,
 * see if you can fix it!
 * Be sure to fix it in the spirit of the code, do not hard code the result.
 */

function troubleshooting() {
    const a = 1;
    const b = 1;

    let result;

    // Edit between these lines
    // =================================
    result = a + b;
    // =================================

    return result;
}

// Do not change this
// module.exports = troubleshooting;

/*
 * Foundations data types and conditionals Assignment
 * Exercise 2
 */
/**
 * The code below tells the browser to ask you for a number
 * then if that number is `6`, it returns `true` otherwise it returns `false`
 *
 * Change this code so it returns `true` when the number is greater than or equal to 10, and false if it is less than 10
 */

number = Number(prompt("enter a number"));

function numberChecker() {
    if (number >= 10) {
        return true;
    } else if (number < 10) {
        return false;
    }
}

/*
 * Foundations data types and conditionals Assignment
 * Exercise 3
 * Lets do some math!
 * Some rules first:
 *   - Replace the strings to the right of the = with the math expression they describe.
 *   - Do not manually enter the answers to the equations. For example, `const a = 9` would be incorrect as 9 is the answer to the equation you're being asked to write out
 */

const a = 1 + 8;
const b = 22 * 3;
const c = 5 % 4;
const d = a - 17;
const e = a + b + c + d;

// module.exports = {a, b, c, d, e}



/*
 * Foundations data types and conditionals Assignment
 * Exercise 4
 * way to large to put it in here, it is in replit.
 */


// function-basics javascript.info
// tasks
// Rewrite the function using '?' or '||'
// The following function returns =true= if the parameter =age= is greater than =18=.
// Otherwise it asks for a confirmation and returns its result.
/*
function checkAge(age) {
    if (age > 18) {
        return true;
    } else {
        return confirm('Did parents allow you?');
    }
}

function checkAge(age) => {
    return (age > 18) ? true : confirm('Did parents allow you?');
}

function min(a, b) {
    if ( a < b ) {
        return a;
    }  else {
        return b;
    }
}

function min(a, b) {
    return a < b ? a : b;
}

function pow(x, n) {
    //return x ** n;
    let result;
    for( let i = 1; result < n.length; i++){
        result*= n[i];
    }
    return result;
}
*/

// arrow-functions-basics javascript.info
// task
// Rewrite with arrow functions
// Replace function Expressions with arrow functions in the code below:
// function ask(question, yes, no) {
//     if (confirm(question)) yes();
//     else no();
// }

let ask = (question, yes, no) => {
    if (confirm(question)) yes();
    else no();
}

// ask(
//     "Do you agree?",
//     function() { alert("You agreed."); },
//     function() { alert("You canceled the execution."); }
// );

ask (
    "do you agree?",
    () => alert("You agreed."),
    () => alert("You canceled the execution.")
);

//function-basics odin-project assignment
function capitalize (string) {
    let lowerString = string.toLowerCase();

    lowerString.split('')
    lowerString.toUpperCase()
    lowerString.join('');

    return prompt(lowerString);
}

let lastLetter =  string => string[-1];





