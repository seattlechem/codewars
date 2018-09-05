// using built-in function (array.reverse)
function solution(str){
  const arr = str.split('');
  arr.reverse();
  return arr.join('');
}

//using for loop
function solution(str){
  let reversed = '';
  for (var k of str){
    reversed = k + reversed;
  }
  return reversed;
}

//using reduce()
function solution(str){
  return str.split('').reduce((reversed, char) => {return char + reversed;}, '');
  
}
