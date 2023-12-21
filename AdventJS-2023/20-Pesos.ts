/* En cada posición, vamos a distribuir la carga de los juguetes en función del número de juguetes de las posiciones vecinas.

Una posición vecina es aquella que está encima, abajo, a la izquierda o a la derecha de la posición actual. Por lo tanto, no se consideran vecinas las posiciones en diagonal.

Escribe una función distributeGifts que reciba una matriz de números representando los juguetes en el trineo y devuelva otra matriz con el mismo tamaño y número de elementos pero donde cada elemento es el promedio de su valor original y los valores de sus vecinos.

Ten en cuenta que hay posiciones que son null y que no contarán para el promedio como vecino pero sí se sustituirá por el valor promedio de sus vecinos.

Ten en cuenta:
- Las matrices no siempre son cuadradas, pueden tener más filas que columnas o viceversa.
- Para redondear los valores, debes utilizar la función Math.round() de JavaScript.
- Los valores null no se tienen en cuenta para el cálculo del promedio pero sí se sustituyen por el valor promedio de sus vecinos.
- Los bordes de la matriz tienen menos vecinos posibles que el resto de posiciones.
- Siempre son números enteros positivos. */

function distributeGifts(weights: (number | null) [][]): number[][] {
  const rows = weights.length;
  const cols = weights[0].length;

  const getNeighbors = (row: number, col: number): number[] => {
    const neighbors: (number | null)[] = [];
    if(row > 0) neighbors.push(weights[row - 1][col]);
    if(row < rows - 1) neighbors.push(weights[row + 1][col]);
    if(col > 0) neighbors.push(weights[row][col - 1]);
    if(col < cols - 1) neighbors.push(weights[row][col + 1]);
    return neighbors.filter((n): n is number => n !== null);
  }

  const result: number[][] = [];

  for(let row = 0; row < rows; row++) {
    const rowResult: number[] = [];
    for(let col = 0; col < cols; col++) {
      const current = weights[row][col] || 0;
      const neighbors = getNeighbors(row, col);
      const sum = neighbors.reduce((acc, n) => acc + n, 0) + current;
      if(current === 0){
        rowResult.push(Math.round(sum / neighbors.length));
      }else{
        rowResult.push(Math.round(sum / (neighbors.length + 1)));
      }
    }
    result.push(rowResult);
  }

  return result;
}

const input = [
  [4, 5, 1],
  [6, null, 3],
  [8, null, 4]
]

distributeGifts(input) // [[5, 3, 3], [6, 5, 3], [7, 6, 4]]