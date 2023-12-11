/* Las luces son de dos colores: 🔴 y 🟢 . Para que el efecto sea el adecuado, siempre deben estar alternadas. Es decir, si la primera luz es roja, la segunda debe ser verde, la tercera roja, la cuarta verde, etc.

Escribir una función adjustLights que, dado un array de strings con el color de cada luz (representados con los emojis 🔴 para el rojo y 🟢 para el verde), devuelva el número mínimo de luces que hay que cambiar para que estén los colores alternos.

adjustLights(['🟢', '🔴', '🟢', '🟢', '🟢']) */
// -> 1 (cambias la cuarta luz a 🔴)

function adjustLights(lights: string[]): number {
  let count = 0;
  for (let i = 0; i < lights.length - 1; i++) {
    if (lights[i] === lights[i + 1]) {
      count++;
      lights[i + 1] = lights[i + 1] === '🔴' ? '🟢' : '🔴';
    }
  }
  return count;
}