// Seleccionar los elementos HTML
const resultado = document.getElementById("resultado") as HTMLElement;
const botones = document.querySelectorAll(".boton");
const operacionSpan = document.getElementById("operacion") as HTMLElement;

// Variables para guardar los estados
let valorActual: string = "";
let valorAnterior: string = "";
let operador: string | null = null;

// Función para actualizar el resultado
const actualizarResultado = (valor: string) => {
  resultado.innerHTML = `<span id="operacion">${operacionSpan.innerHTML}</span> ${valor}`;
};

//Función para acutalizar el span de operación
const actualizarSpanOperacion = () => {
  if (operador) {
    operacionSpan.innerHTML = `${valorAnterior}${operador}${valorActual}`;
  } else {
    operacionSpan.innerHTML = `${valorActual}`;
  }
};

// Cuando el usuario presiona un botón
const manejarClickBoton = (valor: string) => {
  // Si es un número o un punto decimal
  if (!isNaN(Number(valor)) || valor === ".") {
    valorActual += valor;
    actualizarSpanOperacion();
    actualizarResultado(valorActual);
  }
  // Si se quiere limpiar la calculadora
  else if (valor === "C") {
    valorActual = "";
    valorAnterior = "";
    operador = null;
    actualizarSpanOperacion();
    actualizarResultado("0");
  }
  // Si se presiona un operador (+, -, *, /)
  else if (["+", "-", "*", "/"].includes(valor)) {
    if (valorActual === "") return;
    // Si hay un operador y un valor anterior
    if (operador && valorAnterior) {
      const resultadoOperacion = eval(
        `${valorAnterior}${operador}${valorActual}`
      );
      valorAnterior = resultadoOperacion.toString();
      actualizarSpanOperacion();
      actualizarResultado(resultadoOperacion.toString());
    } else {
      valorAnterior = valorActual;
      operacionSpan.innerHTML = `${valorAnterior}${valor}`;
    }
    valorActual = "";
    operador = valor;
    actualizarSpanOperacion();
  }
  // Si se presiona el botón de igual
  else if (valor === "=") {
    if (valorAnterior && operador && valorActual) {
      const resultadoOperacion = eval(
        `${valorAnterior}${operador}${valorActual}`
      );
      actualizarSpanOperacion();
      valorAnterior = resultadoOperacion.toString();
      actualizarResultado(resultadoOperacion.toString());
    }
    operador = null;
    valorActual = "";
  }
};

// Asignar el evento click a cada botón
botones.forEach((boton) => {
  boton.addEventListener("click", () => {
    const valor = boton.getAttribute("data-value")!;
    console.log(valor);
    manejarClickBoton(valor);
  });
});
