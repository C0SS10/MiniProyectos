/* Estamos creando una función a la que le pasamos: el almacén 🏬 que deben navegar y los movimientos ↔️ que pueden realizar.

El almacén se representa como un array de cadenas de texto, donde:

. significa que hay vía libre.
* significa que hay un obstáculo.
! es la posición inicial del robot.
Los movimientos son un array de cadenas de texto, donde:

R mueve al robot una posición a la derecha.
L mueve al robot una posición a la izquierda.
U mueve al robot una posición hacia arriba.
D mueve al robot una posición hacia abajo.
Hay que tener en cuenta que el robot no puede superar los obstáculos ni los límites del almacén.

Dados un almacén y los movimientos, debemos devolver el array con la posición final de nuestro robot.
Ten en cuenta que la store es un array que puede ser de un número de filas que va de 1 a 100, ya que tenemos almacenes de todos los tamaños.
También que el robot es posible que termine en su posición inicial si no puede moverse o si está dando vueltas. */

function autonomousDrive(store: string[], movements: string[]): string[]{
  const numRows = store.length
  if(numRows === 0) return []

  const numCols = store[0].length
  const storeGrid = store.map(row => row.split(''))
  let robotPosition: {row: number, col: number} | null = null

  // Find the initial position of the robot
  for(let row = 0; row < numRows; row++){
    const col = store[row].indexOf('!')
    if(col !== -1){
      robotPosition = {row, col}
      break
    }
  }

  // If the robot is not in the store, return the store
  if(!robotPosition) return store

  const moveRobot = (movement: string): void => {
    const {row, col} = robotPosition!
    switch(movement){
      case 'R':
        if(col + 1 < numCols && storeGrid[row][col + 1] === '.'){
          storeGrid[row][col] = '.'
          storeGrid[row][col + 1] = '!'
          robotPosition = {row, col: col + 1}
        }
        break;
      case 'L':
        if(col - 1 >= 0 && storeGrid[row][col - 1] === '.'){
          storeGrid[row][col] = '.'
          storeGrid[row][col - 1] = '!'
          robotPosition = {row, col: col - 1}
        }
        break;
      case 'U':
        if(row - 1 >= 0 && storeGrid[row + 1][col] === '.'){
          storeGrid[row][col] = '.'
          storeGrid[row - 1][col] = '!'
          robotPosition = {row: row - 1, col}
        }
        break;
      case 'D':
        if(row + 1 < numRows && storeGrid[row + 1][col] === '.'){
          storeGrid[row][col] = '.'
          storeGrid[row + 1][col] = '!'
          robotPosition = {row: row + 1, col}
        }
        break;
    }
  }

  for(const movement of movements){
    moveRobot(movement)
  }

  return storeGrid.map(row => row.join(''))
}

// const store = ['..!....', '...*.*.']

// const movements = ['R', 'R', 'D', 'L']
// const result = autonomousDrive(store, movements)
// console.log(result)
// [
//   ".......",
//   "...*!*."
// ]
// El último movimiento es hacia la izquierda, pero no puede moverse porque hay un obstáculo.