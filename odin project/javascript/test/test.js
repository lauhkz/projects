/*
console.log(Number(undefined));
console.log(typeof(NaN));
console.log(NaN == 0)
*/
// What will be the result of these expressions
/*
console.log(5 > 4)                    //true   = true
console.log("apple" > "pineapple")    //true?  = false dictionary comparison, "a" is smaller than "p"
console.log("2" > "12")               //false  = true  dictionary comparison, first char "2" is greater than the first char "1"
console.log(undefined == null)        //true   = true null and undefined equal each other only
console.log(undefined === null)       //false = false strict equality is strict, different types from both sides lead to false
console.log(null == "\n0\n")          //true  = false null ONLY equals undefined
console.log(null === +"\n0\n")        //false = false Strict equality

alert( null || undefined || 0); this return the last case

let firstName = "";
let lastName = "";
let nickName = "";

alert( firstName || lastName || nickName || "Anonymous"); Returns "Anonymous"

 alert( null || 2 || undefined) returns 2, because is the last truthy value
Write the code which asks for a login with prompt.

If the visitor enters "Admin", then prompt for a password, if the input is an empty line or Esc – show “Canceled”, if it’s another string – then show “I don’t know you”.

The password is checked as follows:

    -[ ] If it equals “TheMaster”, then show “Welcome!”,
    -[ ] Another string – show “Wrong password”,
    -[ ] For an empty string or cancelled input, show “Canceled”


let user = prompt( "who is there?")         //user what? the name of the variable should be precise for what it ask for
if (user == "Admin") {
    let pass = prompt( "password")
    if (pass == "TheMaster"){
        alert ( "Welcome" )
    } else if (pass == null || pass == ""){
        alert ( "Canceled" )
    } else {
    alert ( "Wrong password" )
    }
} else if (user == null || user == ""){
    alert ( "Canceled" )
} else {
    alert("I don't know you")
}
*/

