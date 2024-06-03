'use strict';

function BinarioADecimal(num) {
    let decimal = parseInt(num,2)
    return decimal;
}

function DecimalABinario(num) {
    let binary = '';
    while (num > 0) {
        binary = (num % 2) + binary;
        num = Math.floor(num / 2);
    }
    return binary
}

module.exports = {
   BinarioADecimal,
   DecimalABinario,
};
