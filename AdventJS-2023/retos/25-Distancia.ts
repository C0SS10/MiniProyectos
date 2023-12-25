/* Los elfos quieren saber cuántos movimientos ha hecho Santa Claus 🛷 para entregar todos los regalos. Para ello, te dan un mapa de la ciudad con la ubicación de cada niño y de Santa.
El mapa es una cadena de texto multi línea donde cada caracter representa una casilla. Los niños se representan por números del 1 al 9 y Santa Claus por la letra S. El resto de casillas son.
Santa Claus sólo puede moverse hacia arriba, abajo, izquierda o derecha, y cada movimiento cuenta como 1 km. Además, siempre empieza en la posición S y debe entregar los regalos en orden, del 1 al 9. 

• El mapa no tiene por qué ser cuadrado.
• El mapa siempre tendrá al menos un niño.
• El mapa siempre tendrá una posición inicial para Santa Claus.
• Los números de los niños nunca se repiten.*/
function travelDistance(map: string): number {
  const mapArray = map.split("\n");
  const children: { [key: string]: [number, number] } = {};
  let santaPosition: [number, number] | null = null;

  mapArray.forEach((line, row) => {
    for (let column = 0; column < line.length; column++) {
      const character = line[column];
      if (character === "S") {
        santaPosition = [row, column];
      } else if (character >= "1" && character <= "9") {
        children[character] = [row, column];
      }
    }
  });

  let totalDistance = 0;
  let currentSantaPosition: [number, number] = santaPosition!;

  for (
    let childNumber = 1;
    childNumber <= Object.keys(children).length;
    childNumber++
  ) {
    const childPosition = children[childNumber];
    totalDistance +=
      Math.abs(childPosition[0] - currentSantaPosition[0]) +
      Math.abs(childPosition[1] - currentSantaPosition[1]);
    currentSantaPosition = childPosition;
  }

  return totalDistance;
}

travelDistance(
  `3....1....
  ..S.......
  .........2
  ..........
  ......4...`
); // 31
