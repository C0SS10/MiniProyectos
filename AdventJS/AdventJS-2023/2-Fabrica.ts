// Tu tarea es escribir una función que, dada una lista de regalos y los materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.
// Un regalo se puede fabricar si contamos con todos los materiales necesarios para fabricarlo.
function manufacture(gifts: string[], materials: string){
  let result: string[] = [];
  materials = materials.toLowerCase();
  gifts = gifts.map(gift => gift.toLowerCase());
  for (let i = 0; i < gifts.length; i++){
    const gift = gifts[i];
    // if the gift has all the letter of the materials
    if (gift.split('').every(letter => materials.includes(letter))){
      result.push(gift);
    }else{
      // if the gift has some of the letters of the materials cant be made
      continue;
    }
  }
  return result;
};

const gifts = ['tren', 'oso', 'pelota'];
const materials = 'tronesa';

manufacture(gifts, materials); // ['tren', 'oso']