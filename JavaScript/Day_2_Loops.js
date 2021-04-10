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

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var x;
    var cons=[]
    for (x in s) {
        if ('aeiou'.includes(s[x])){
            console.log(s[x])    
        }
        else{
            cons.push(s[x])
        }   
}
for (x in cons) {
  console.log(cons[x]) 
}
    
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}