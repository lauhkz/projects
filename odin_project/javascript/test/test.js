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
*/
// Tasks
// Working with variables
// - Declare two variables: admin and name.
// - Assign the value "John" to name.
// - Copy the value from name to admin.
// - Show the value of admin using alert (must output "john").

let admin;
    name;
name = 'john';
admin = name;
alert(admin);

// Giving the right name
// - Create a variable with the name of our planet. How would you name such a variable?
// - Create a variable to store the name of a current visitor to a website. How would you name that variable?
let ourPlanetName = "Earth";
let currentUserName;

// Uppercase const?
// Would it be right to use upper case for birthday? For age? Or even for both?
// const BIRTHDAY = '18.04.1982'; // make birthday uppercase?
// const AGE = someCode(BIRTHDAY); // make age uppercase?
// uppercase is only right to use in the birthday variable because the value is already known before the execution

// Basic operators .. javascript.info

// String concatenation with binary +
// usually the plus operator + sums numbers.
// But, if the binary + is applied to strings, it merges (concatenates) them:

let s = "my" + "string";
alert(s); // mystring
alert( '1' + 2 ); // "12"
alert( 2 + 2 + '1' ); // '41' and not '221'

// the binary + is the only opetors that supports strings in such a way. Other arithmetic operators work only with
// numbers and always convert their operands to numbers
// here's the demo for substraction and division:
alert( 6 - '2' ); // 4, converts '2' to a number
alert( '6' / '2' ); // 3, converts both operands to numbers

// TASKS
// The postfix and prefix forms
// What are the final values of all variables a, b, c, and d after the code below?
let a = 1, b = 1;

let c = ++a; // ? i think this would return 2
let d = b++; // ? and this would return 1

alert(a)   // returns 2
alert(b)   // returns 2

// Assignment result
// What are the values of a and x after the code below?

let a = 2;

let x = 1 + (a *= 2);

alert(a);  // returns 4
alert(x);  // returns 5

// Type conversions
// What are results of these expressions?

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

// 1. null becomes 0 after the numeric conversion.
// 2. undefined becomes NaN after the numeric conversion.
// 3. Space characters are trimmed off string start and end
// when a string is converted to a number. Here the whole string
// consists of space characters, such as \t, \n and a "regular" space
// between them. So, similarly to an empty string, it becomes 0.

