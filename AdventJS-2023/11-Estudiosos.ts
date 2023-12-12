/* Un palíndromo es una palabra que se lee igual hacia adelante y hacia atrás. Los elfos quieren saber si es posible formar un palíndromo haciendo, como mucho, un intercambio de letras.

Crea una función getIndexsForPalindrome que reciba una cadena de caracteres y devolverá:

Si ya es un palíndromo, un array vacío.
Si no es posible, null.
Si se puede formar un palíndromo con un cambio, un array con las dos posiciones (índices) que se deben intercambiar para poder crearlo.
Por ejemplo: */

// getIndexsForPalindrome('anna') // []
// getIndexsForPalindrome('abab') // [0, 1]
// getIndexsForPalindrome('abac') // null
// getIndexsForPalindrome('aaaaaaaa') // []
// getIndexsForPalindrome('aaababa') // [1, 3]
// getIndexsForPalindrome('caababa') // null
// Si se puede formar el palíndromo con diferentes intercambios, siempre se debe devolver el primero que se encuentre.

function getIndexsForPalindrome(word: string): number[] | null {
  let count = 0;
  let arrayWord = word.split("");
  let index = 1;
  let result: number[] = [];
  let charFailed = "";
  let positionFailed2 = -1;

  for (let i = 0; i < arrayWord.length / 2; i++) {
    if (arrayWord[i] === arrayWord[arrayWord.length - i - 1]) {
      index = 1;
      count++;
    } else {
      if (charFailed === "") {
        charFailed = arrayWord[i];
        positionFailed2 = arrayWord.length - i - 1;
      }
      if (arrayWord[i] !== charFailed) {
        if (
          word[i] === word[Math.floor(word.length / 2)] &&
          word.length % 2 === 1
        ) {
          return [Math.floor(word.length / 2), positionFailed2];
        } else {
          return null;
        }
      } else {
        const temp = arrayWord[i];
        arrayWord[i] = arrayWord[i + index];
        arrayWord[i + index] = temp;
        result = [i, i + index];
        i--;
        index++;
      }
    }
  }
  return result;
}