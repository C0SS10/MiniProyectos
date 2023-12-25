// la secuencia original de pasos en la fabricación original y la secuencia modificada modified que puede incluir un paso extra o faltar un paso.
// escribir una función que identifique y devuelva el primer paso extra que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia entre las secuencias, devuelve una cadena vacía.

function findNaughtyStep(original: string, modified: string): string {
  const minLength = Math.min(original.length, modified.length);

  for (let i = 0; i < minLength; i++) {
    if (original[i] !== modified[i]) {
      // Encuentra el primer carácter diferente y determina en qué cadena está
      return original.length > modified.length
        ? original[i]
        : modified[i];
    }
  }

  // Si las longitudes son diferentes, devuelve el carácter adicional o faltante
  return original.length > modified.length
    ? original.slice(minLength)
    : modified.slice(minLength);
}

const original = 'abcd'
const modified = 'abcde'
console.log(findNaughtyStep(original, modified))// 'e'