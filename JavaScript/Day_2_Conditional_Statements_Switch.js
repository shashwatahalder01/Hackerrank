'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    let a=s.charAt(0)
    switch(true) {
  case 'aeiou'.includes(a):
    letter='A'
    break;
  case 'bcdfg'.includes(a):
    letter='B'
    break;
  case 'hjklm'.includes(a):
    letter='C'
    break;
  case 'npqrstvwxyz'.includes(a):
    letter='D'
    break;
  default:    
}
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}