function count (string) {  
  // The function code should be here
  const charDict = {};
  for (let i of string){
    charDict[i] = charDict[i] + 1 || 1;
  }
  return charDict;
}


// Best practice solution
function bestCount (string) {
  var count = {};
  string.split('').forEach(function(s) {
    count[s] ? count[s]++ : count[s] = 1;
  });
  return count;
}
