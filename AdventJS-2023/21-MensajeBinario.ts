/* El mensaje que llega es un array de 0s y 1s. Parece que han encontrado un patrón… Para asegurarse, quieren encontrar el segmento más largo de la cadena donde el número de 0s y 1s sea igual.
Ten en cuenta que si hay más de un patrón equilibrado, debes devolver el más largo y el primero que encuentres de izquierda a derecha. */
function findBalancedSegment(message: number[]): number[] {
  const prefixSum: number[] = [0];
  let sum = 0;

  for (const num of message) {
    sum += num === 0 ? -1 : 1;
    prefixSum.push(sum);
  }

  const sumIndexMap: Record<number, number> = { 0: 0 };
  let maxLength = 0;
  let startIndex = -1;
  let endIndex = -1;

  for (let i = 0; i < prefixSum.length; i++) {
    const currentSum = prefixSum[i];
    if (sumIndexMap[currentSum] !== undefined) {
      const currentLength = i - sumIndexMap[currentSum];
      if (currentLength > maxLength) {
        maxLength = currentLength;
        startIndex = sumIndexMap[currentSum];
        endIndex = i;
      }
    } else {
      sumIndexMap[currentSum] = i;
    }
  }

  if (startIndex !== -1 && endIndex !== -1) {
    return [startIndex, endIndex - 1];
  }

  return [];
}


findBalancedSegment([1, 1, 0, 1, 1, 0, 1, 1])
//                         |________|
// posición del segmento:    [2, 5]
// más largo equilibrado
// de 0s y 1s

findBalancedSegment([1, 1, 0])
//                      |__|
//                     [1, 2]

findBalancedSegment([1, 1, 1])
// no hay segmentos equilibrados: []