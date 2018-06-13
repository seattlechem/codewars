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

