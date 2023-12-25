// Escribir una función que tome una cadena de texto y revierta los caracteres
// dentro de cada par de paréntesis, eliminando los paréntesis en el mensaje final.
// Eso sí, ten en cuenta que pueden existir paréntesis anidados, por lo que debes
// invertir los caracteres en el orden correcto.

function decode(message: string): string {
  const stack: string[] = [];
  let currentWord: string = "";
  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    if (char == "(") {
      stack.push(currentWord);
      currentWord = "";
    } else if (char == ")") {
      const lastWord = stack.pop() || "";
      currentWord = lastWord + currentWord.split("").reverse().join("");
    } else {
      currentWord += char;
    }
  }
  return currentWord + (stack.pop() || "");
}

const a = decode("hola (odnum)");
console.log(a); // hola mundo

const b = decode("(olleh) (dlrow)!");
console.log(b); // hello world!

const c = decode("sa(u(cla)atn)s");
console.log(c); // santaclaus
