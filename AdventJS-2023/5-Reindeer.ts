/* La carretera se representa con una cadena de caracteres, donde:

. = Carretera
S = Trineo de Santa
* = Barrera abierta
| = Barrera cerrada
Ejemplo de carretera: S...|....|.....

Cada unidad de tiempo, el trineo avanza una posición a la derecha. Si encuentra una barrera cerrada, se detiene hasta que la barrera se abra. Si está abierta, la atraviesa directamente.

Todas las barreras empiezan cerradas, pero después de 5 unidades de tiempo, se abren todas para siempre.*/


function cyberReindeer(road: string, time: number): string[] {
  let result: string[] = [road];
  let currentPosition = 0;
  let currentSymbol = ".";

  for (let i = 1; i < time; i++) {
    if (i === 5) {
      road = road.replace(/\|/g, "*");
    }

    const newRoad = road.replace(/S[\.\*]/, `${currentSymbol}S`);

    if (newRoad !== road) {
      currentPosition++;
      currentSymbol = road[currentPosition];
    }

    road = newRoad;
    result.push(road);
  }

  return result;
}
