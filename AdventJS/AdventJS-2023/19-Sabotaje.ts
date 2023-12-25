/* Los * representan los juguetes saboteados y las celdas vacías con un espacio en blanco son los lugares seguros.
Escribir una función que devuelva la misma matriz pero, en cada posición, nos indique el número de juguetes saboteados que hay en las celdas adyacentes. Si una celda contiene un juguete saboteado, debe permanecer igual. Si una celda no toca ningún juguete saboteado, debe contener un espacio en blanco.

Las celdas diagonales también se consideran adyacentes.
El tablero siempre tendrá al menos una celda vacía y un juguete saboteado *.
El tablero puede tener cualquier tamaño.
Los números son cadenas de texto. */

function revealSabotage(store: string[][]): string[][]{
  const rows = store.length
  const cols = store[0].length

  const incrementCell = (row: number, col: number) => {
    if(row >= 0 && row < rows && col >= 0 && col < cols){
      if(store[row][col] === ' '){
        store[row][col] = '1'
      }else if(store[row][col] !== '*'){
        store[row][col] = (parseInt(store[row][col]) + 1).toString()
      }
    }
  }

  for(let row = 0; row < rows; row++){
    for(let col = 0; col < cols; col++){
      if(store[row][col] === '*'){
        incrementCell(row - 1, col - 1)
        incrementCell(row - 1, col)
        incrementCell(row - 1, col + 1)
        incrementCell(row, col - 1)
        incrementCell(row, col + 1)
        incrementCell(row + 1, col - 1)
        incrementCell(row + 1, col)
        incrementCell(row + 1, col + 1)
      }
    }
  }

  return store
}

 const store = [
  ['*', ' ', ' ', ' '],
  [' ', ' ', '*', ' '],
  [' ', ' ', ' ', ' '],
  ['*', ' ', ' ', ' ']
]

console.log(revealSabotage(store))
/* Debería mostrar:
[
    ['*', '2', '1', '1'],
    ['1', '2', '*', '1'],
    ['1', '2', '1', '1'],
    ['*', '1', ' ', ' ']
]
*/ 