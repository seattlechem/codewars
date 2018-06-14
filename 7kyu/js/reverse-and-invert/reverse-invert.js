function reverseInvert(array){
  let res = [];
  for (let i = 0; i < array.length; i++){
    if (typeof array[i] === 'number' && array[i] % 1 === 0){
      res.push(-parseInt(Math.abs(array[i]).toString().split('').reverse().join('')) * Math.sign(array[i]));
    }
  }
  return res;
}

function otherReverseInvert(array) {
  return array
    .filter(n => Number.isInteger(n))
    .map(n => -Math.sign(n) * parseInt(String(n).split("").reverse().join(""), 10));
}
