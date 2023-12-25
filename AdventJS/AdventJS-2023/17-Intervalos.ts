/* Cada intervalo se representa como un array de dos elementos, donde el primer elemento es el inicio del alquiler y el segundo es el final.

Por ejemplo, el array [2, 7] representa un alquiler que comienza en la hora 2 y termina en la hora 7. El problema es que a veces los intervalos se superponen entre sí, haciendo que sea un lío entender de qué hora a qué hora se alquiló el trineo. Escribir una función que fusione todos los intervalos superpuestos y devolver un array de intervalos ordenados */
function optimizeIntervals(intervals: number[][]): number [][] {
  intervals.sort((a, b) => a[0] - b[0])
  const mergedIntervals: number[][] = []
  let currentInterval: number[] = intervals[0]

  for (let i = 1; i < intervals.length; i++) {
    const nextInterval = intervals[i]
    if (currentInterval[1] >= nextInterval[0]) {
      currentInterval[1] = Math.max(currentInterval[1], nextInterval[1])
    } else {
      mergedIntervals.push([...currentInterval])
      currentInterval = nextInterval
    }
  }
  mergedIntervals.push([...currentInterval])
  return mergedIntervals
}