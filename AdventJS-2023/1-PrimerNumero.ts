// si hay más de un número repetido, debes devolver el número cuya segunda ocurrencia aparezca primero en la lista. Si no hay números repetidos, devuelve -1

function findFirstRepeated(gifts: number[]) {
  let repeated: number[] = [];
  for (let i = 0; i < gifts.length; i++) {
    if (repeated.includes(gifts[i])) {
      return gifts[i];
    } else {
      repeated.push(gifts[i]);
    }
  }
  return -1;
}
