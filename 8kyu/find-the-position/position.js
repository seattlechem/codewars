// https://www.codewars.com/kata/find-the-position/train/javascript

function position(letter){
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const alpha = alphabet.split('');

  let indexNum = alpha.indexOf(letter) + 1;

  return `Position of alphabet: ${indexNum}`;
}

// position = l => `Position of alphabet: ${l.charCodeAt() - 96}`;