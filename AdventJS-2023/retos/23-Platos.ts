/* Te da una lista de platos navideños donde cada elemento consiste en una lista de strings que comienza con el nombre del plato, seguido de todos los ingredientes utilizados para su preparación. Tienes que escribir una función que agrupe los platos por ingredientes siempre que haya al menos 2 platos que los contengan. Así que devolvemos un array de arrays donde la primera posición es el nombre del ingrediente y el resto los nombres de los platos. Tanto la lista de ingredientes como los platos deben estar ordenados alfabéticamente.

• Todos los nombres de los platos son diferentes.
• Los nombres de los ingredientes para un plato dado son distintos entre sí.
• Si no hay ingredientes repetidos, devolvemos un array vacío.*/
function organizeChristmasDinner(dishes: string[][]): string[][] {
  const ingredientsMap: Map<string, string[]> = new Map();

  for (const dish of dishes) {
    const [dishName, ...ingredients] = dish;
    for (const ingredient of ingredients) {
      if (!ingredientsMap.has(ingredient)) {
        ingredientsMap.set(ingredient, [ingredient, dishName]);
      } else {
        ingredientsMap.get(ingredient)!.push(dishName);
      }
    }
  }

  const result: string[][] = Array.from(ingredientsMap.values())
    .filter((group) => group.length > 2)
    .sort((a, b) => a[0].localeCompare(b[0]));

  for (let i = 0; i < result.length; i++) {
    result[i] = [result[i][0], ...result[i].slice(1).sort((a, b) => a.localeCompare(b))];
  }

  return result;
}

organizeChristmasDinner([
  ["christmas turkey", "turkey", "sauce", "herbs"],
  ["cake", "flour", "sugar", "egg"],
  ["hot chocolate", "chocolate", "milk", "sugar"],
  ["pizza", "sauce", "tomato", "cheese", "ham"],
]);

organizeChristmasDinner([
  ["fruit salad", "apple", "banana", "orange"],
  ["berry smoothie", "blueberry", "banana", "milk"],
  ["apple pie", "apple", "sugar", "flour"],
]);
