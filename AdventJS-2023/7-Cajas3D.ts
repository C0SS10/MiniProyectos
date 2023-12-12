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
  const append = (current: string, line: string, spaces: number): string =>
    `${" ".repeat(spaces)}${line}\n${current}\n${line}`;

  const sizeDifference = size - 2;

  const middleSymbolCount = sizeDifference >= 0 ? sizeDifference : 0;
  let draw: string = `${"#".repeat(size)}${symbol.repeat(middleSymbolCount)}${
    sizeDifference >= 0 ? "#" : ""
  }`;

  for (
    let symbolCount = sizeDifference, spaces = 1;
    symbolCount > 0;
    symbolCount--, spaces++
  ) {
    const line: string = `#${symbol.repeat(sizeDifference)}#${symbol.repeat(
      symbolCount - 1
    )}#`;
    draw = append(draw, line, spaces);
  }

  if (size > 1) {
    const end: string = "#".repeat(size);
    draw = append(draw, end, size - 1);
  }

  return `${draw}\n`;
}
