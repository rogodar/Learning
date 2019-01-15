function grades(input) {
    let number = input[0];
    if (number >= 5.50){
        console.log('Your grade is A');
    }else if(number >= 4.50){
        console.log('Your grade is Verry good');
    }else if(number >= 3.00){
        console.log('Your grade is Good');
    }else{
        console.log('Your grade is BAD - Try again')
    }
}

grades([3.0]);