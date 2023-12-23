/* Han creado un sistema de instrucciones simple y necesitan tu ayuda para construir un compilador que interprete estos símbolos.

El compilador trabaja con un contador que inicialmente tiene un valor de 0. Las instrucciones modificarán el valor de este contador.

Instrucciones del lenguaje de los elfos en base a símbolos:

+: Incrementa en 1 el valor del contador.
*: Multiplica por 2 el valor del contador.
-: Resta 1 al valor del contador.
%: Marca un punto de retorno. No modifica el contador.
<: Vuelve atrás una vez a la última instrucción con el símbolo % que haya visto. Si no hay un % previo, no hace nada.
¿: Inicia un bloque condicional que se ejecuta si el contador es mayor a 0.
?: Finaliza un bloque condicional. */
function compile(code: string): number {
  let result: number = 0;
  const returnStack: number[] = [];

  for (let i = 0; i < code.length; i++) {
    switch (code[i]) {
      case '+':
        result++;
        break;
      case '*':
        result *= 2;
        break;
      case '-':
        result--;
        break;
      case '%':
        if (returnStack.length > 0) {
          returnStack.pop();
        }
        returnStack.push(i);
        break;
      case '<':
        if (returnStack.length > 0) {
          i = returnStack.pop()!;
        }
        break;
      case '¿':
        if (result <= 0) {
          let nestedCount = 1;
          while (nestedCount > 0) {
            i++;
            if (code[i] === '¿') {
              nestedCount++;
            } else if (code[i] === '?') {
              nestedCount--;
            }
          }
        }
        break;
      case '?':
        break;
      default:
        break;
    }
  }

  return result;
}

compile('<%+¿++%++<?') // 7