// Escribir una función que, dado un tamaño n (entero), genere un dibujo de un regalo en 3D utilizando caracteres ASCII.
// Las líneas de los regalos se dibujan con # y las caras con el símbolo que nos pasan como parámetro:
// Importante: Nos han dicho que siempre hay que dejar un salto de línea al final del dibujo.
// Nota: Ten en cuenta que, en los tests, la primera línea se ve empujada por el caracter ".

/* Test: drawGift(4, "+")

Expected:
"   ####
  #++##
 #++#+#
####++#
#++#+#
#++##
####
" */

function drawGift(size: number, symbol: string): string {
  let result = "";
  let spaces = size;
  let symbols = 1;

  for (let i = 0; i < size; i++) {
    result += " ".repeat(spaces) + symbol.repeat(symbols) + "\n";
    spaces--;
    symbols += 2;
  }

  spaces = 0;
  symbols = size * 2 + 1;

  for (let i = 0; i < size; i++) {
    result += " ".repeat(spaces) + symbol.repeat(symbols) + "\n";
    spaces++;
    symbols -= 2;
  }

  return result;
}
