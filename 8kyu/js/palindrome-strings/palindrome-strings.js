function isPalindrome(line) {
  // create array in string
  var str = ("" + line).split("");
  var reversed = "";
  for (var i of str){
    reversed = i + reversed;
  }
  line = ("" + line);
  return line === reversed;
}

// best practice solution
function isPalindrome(line) {
  return (String(line) === String(line).split('').reverse().join('') );
}

//  using every()
function isPalindrome(line) {
  line = String(line).split("");
  return line.every((char, i) => {
    return char === line[line.length - i - 1];
  })
}

