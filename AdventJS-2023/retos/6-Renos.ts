/* > = Avanza a la derecha
< = Avanza a la izquierda
* = Puede avanzar o retroceder

En el ejemplo >>*<, la máxima distancia que recorre el reno es 2. Va a la derecha dos veces +2, luego con el * puede ir a la derecha otra vez para maximizar la distancia +1 y luego va a la izquierda -1.

Crea una función maxDistance que reciba la cadena de texto movements y devuelva la máxima distancia que puede recorrer el reno en cualquier dirección: */

function maxDistance(movements: string): number {
  let distance = 0;

  let right = (movements.match(/>/g) || []).length;
  let left = (movements.match(/</g) || []).length;

  distance += right;
  distance -= left;

  let extra = movements.length - (right + left);

  return Math.abs(distance) + extra;
}