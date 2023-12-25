/* Las luces son de dos colores: 🔴 y 🟢 . Para que el efecto sea el adecuado, siempre deben estar alternadas. Es decir, si la primera luz es roja, la segunda debe ser verde, la tercera roja, la cuarta verde, etc.

Escribir una función adjustLights que, dado un array de strings con el color de cada luz (representados con los emojis 🔴 para el rojo y 🟢 para el verde), devuelva el número mínimo de luces que hay que cambiar para que estén los colores alternos. */

function adjustLights(lights: string[]): number {
  let count = 0;
  for (let i = 0; i < lights.length; i++) {
    if (lights[i] === lights[i + 1]) {
      count++;
      lights[i + 1] = lights[i + 1] === '🔴' ? '🟢' : '🔴';
    }
  }
  return count;
}

console.log(adjustLights(['🔴', '🟢', '🔴', '🟢', '🔴', '🟢'])); //0
console.log(adjustLights(['🔴', '🔴', '🔴', '🔴'])); //2
console.log(adjustLights(['🟢', '🟢', '🟢', '🟢'])); //2
console.log(adjustLights(['🟢', '🔴', '🔴', '🟢'])); //2
console.log(adjustLights(['🔴', '🟢', '🟢', '🔴'])); //2