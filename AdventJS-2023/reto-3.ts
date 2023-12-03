// la secuencia original de pasos en la fabricación original y la secuencia modificada modified que puede incluir un paso extra o faltar un paso.
// escribir una función que identifique y devuelva el primer paso extra que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia entre las secuencias, devuelve una cadena vacía.

function findNaughtyStep(original: string, modified: string){
  const minLength = Math.min(original.length, modified.length);

  for (let i = 0; i < minLength; i++) {
    if (original[i] !== modified[i]) {
      // Encuentra el primer carácter diferente y lo devuelve
      return modified[i];
    }
  }

  // Si las longitudes son diferentes, devuelve el carácter adicional o faltante
  if (original.length > modified.length) {
    return original.slice(minLength);
  } else if (original.length < modified.length) {
    return modified.slice(minLength);
  }

  // Si no hay ninguna diferencia, devuelve una cadena vacía
  return '';
}

const original = 'abcd'
const modified = 'abcde'
findNaughtyStep(original, modified) // 'e'