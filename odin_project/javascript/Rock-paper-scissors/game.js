function getComputerChoice(){
    //have 3 options Rock, paper and scissors
    //the computer has to randomly pick one of it and return it
    var options = [
     'rock',
     'paper',
     'scissors'
    ];
    var randomNumber = Math.floor(Math.random()*options.length);

    return options[randomNumber]
};
function playRound(playerSelection, computerSelection){
    let player = playerSelection.toLowerCase();
    let computer = computerSelection
    if (player === computerSelection) {
        return "tie"
    }
    if (player === "rock"){
        if ( computer === "rock"){
            return "You Lose! Paper beats rock"
        } else if ( computer === "scissors"){
            return "You Win! Rock beats scissors"
        } 
    } else if (player === "paper"){
         if ( computer === "scissors"){
            return "You Lose! scissors beats paper"
        } else if ( computer === "rock"){
            return "You Win! paper beats rock"
        }
    } else if (player === "scissors"){
        if ( computer === "scissors"){
            return "You Win! scissors beats paper"
        }  else if ( computer === "rock"){
            return "You Lose! rock beats scissors"
        }
    }
}
const computerSelection = getComputerChoice();
playerSelection = "sCissOrs"
console.log(playRound(playerSelection, computerSelection))


