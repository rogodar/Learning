// function test(input){
//     let number = input[1];
    
//     if(number%2===0){
//         console.log('even')
//     }
//     else{
//         console.log('odd')
//     }
// }

// test([5,6]);

function test(input) {
    let firstNumber=input[0];
    let secondNumber=input[1];
    if(firstNumber>secondNumber){
        console.log(firstNumber);
    }else if(firstNumber<secondNumber){
        console.log(secondNumber);
    }else{
        console.log(firstNumber, "is equal to " ,secondNumber);
    }
}

test([10,10]);