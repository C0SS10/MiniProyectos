/* detectar si una carta es una copia de otra. Las cartas son muy largas y no puedes leerlas, pero puedes compararlas con un algoritmo.

Existe una gran probabilidad de que un caracter se degrade en cada copia (¡no pasa siempre!). Y al ocurrir, la regla que sigue es:

Los caracteres de la A a la Z se degradan de mayúsculas a minúsculas (A-Z ⇒ a-z)
Las letras se degradan en una serie de caracteres en este orden: a-z ⇒ # ⇒ + ⇒ : ⇒ . ⇒
Los caracteres que no son letras (como los dígitos) no se degradan.
Sabiendo esto y recibiendo la carta original y la copia, debes determinar si la copia es una copia de la original.

checkIsValidCopy(
  'Santa Claus is coming',
  'sa#ta cl#us is comin#'
) // true
checkIsValidCopy(
  'Santa Claus is coming',
  'p#nt: cla#s #s c+min#'
) // false (por la p inicial)
checkIsValidCopy('Santa Claus', 's#+:. c:. s') // true
checkIsValidCopy('Santa Claus', 's#+:.#c:. s') // false */

function checkIsValidCopy(original: string, copy: string): boolean {
  const nonLetters: string = "#+:. ";
  const isAncestor = (original: string, copy: string): boolean => {
    const originalIndex: number = nonLetters.indexOf(original);
    const copyIndex: number = nonLetters.indexOf(copy);

    return (
      original === copy ||
      (0 <= originalIndex && 0 <= copyIndex && originalIndex <= copyIndex) ||
      (original.match(/[a-z]/i) && 0 <= copyIndex) ||
      original.toLowerCase() === copy
    );
  };

  if (original.length !== copy.length) return false;

  for (let i = 0; i < original.length; i++) {
    if (!isAncestor(original[i], copy[i])) return false;
  }
  
  return true;
}
