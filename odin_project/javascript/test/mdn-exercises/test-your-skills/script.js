// 1st exercise
const names = ['Chris', 'Li Kang', 'Anne', 'Francesca', 'Mustafa', 'Tina', 'Bert', 'Jada']
function randomName() {
    let randomNumber = '';
    //randomNumber = Math.floor(Math.random() * 8); //wrong approach, i'd use the length method
    randomNumber = Math.floor(Math.random() * names.length);
    para.textContent = names[randomNumber];
}

/*
 3rd exercise
    1. ~~Refactor the code that generates the random number into a separate function called random(),
   which takes as parameters two generic bounds that the random number should be between,
   and returns the result.~~
    2. Update the chooseName() function so that it makes use of the random number function,
   takes the array to choose from as a parameter (making it more flexible), and returns the result.
    3. Print the returned result into the paragraph (para)'s textContent.
*/
const names = ['Chris', 'Li Kang', 'Anne', 'Francesca', 'Mustafa', 'Tina', 'Bert', 'Jada'];

function random(min, max) {
    const number = Math.floor(Math.random() * (max - min)) + min;
    return number;
}

function chooseName(array) {
    //return para.textContent(array[random()]);
    //wrong approach
    const choice = array[random(0, array.length)];
    return choice;
}

para.textContent = chooseName(names);

// exercise 4th
// function isShort(name) {
//     return name.length < 5;
// }

// const shortNames = names.filter(isShort);
// para.textContent = shortNames;

//function isShort(name) => name.length < 5

// make the filter as an anonymous function inside the arrow function
// almost (in the idea, the solution is wrong tho lol) function filterNames(names) => names.filter(function() => names.length < 5)
const filteredNames = names.filter((name) => name.length < 5);
para.textContent = filteredNames;
