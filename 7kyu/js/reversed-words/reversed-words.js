function reverseWords(str) {
  var reversed_words = [];
  var split_space = str.split(' ');
  for (var k of split_space){
    var reversed = '';
    for (var j of k){
      reversed = j + reversed;
    }
    reversed_words.push(reversed);
  }
  return reversed_words.join(' ');
}
