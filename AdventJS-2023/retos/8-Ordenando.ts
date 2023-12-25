/* - Cada 10 regalos del mismo tipo se empaquetan en una caja, representada por {x}. Por ejemplo, 20 regalos tipo a se empaquetan en 2 cajas así: {a}{a}.
- Cada 5 cajas se apilan en un palé, representado por [x]. Por ejemplo, 10 cajas de a se apilan en 2 palés de esta manera: [a][a]
- Cualquier regalo adicional se coloca en una bolsa, representada por () y se colocan todas dentro. Por ejemplo 4 regalos de b se colocan en una bolsa así (bbbb)

Los regalos luego se colocan en el siguiente orden: palés, cajas y bolsas. Y los regalos aparecen en el mismo orden que la cadena de entrada. Tu tarea es escribir una función organizeGifts que tome una cadena de regalos como argumento y devuelva una cadena representando el almacén. */

function organizeGifts(gifts: string): string {
  const countGifts = gifts.match(/\d+/g);
  const nameGifts = gifts.match(/[a-z]/g);

  if (!countGifts || !nameGifts) {
    return '';
  }

  let result = '';
  let countBox = 0;

  for (let countStr of countGifts) {
    const letter = nameGifts[countBox];
    let count: number = parseInt(countStr, 10);

    let x: string = '';

    x += `[${letter}]`.repeat(count / 50);
    count %= 50;

    x += `{${letter}}`.repeat(count / 10);
    count %= 10;

    x += `(${letter.repeat(count)})`.repeat(+!!count);

    result += x;
    countBox++;
  }

  return result;
}
