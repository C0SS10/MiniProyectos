"use strict";

// Seleccionar los elementos HTML
const resultadoElement = document.getElementById("resultado");
const operacionElement = document.getElementById("operacion");
const botones = document.querySelectorAll(".boton");

// Variables para guardar los estados
let valorActual = "";
let valorAnterior = "";
let operador = null;
let resultadoMostrado = false;

// Asignar el evento click a cada botón
botones.forEach((boton) => {
    boton.addEventListener("click", () => manejarClickBoton(boton.getAttribute("data-value")));
});

// Función para actualizar el resultado y la operación en pantalla
const actualizarPantalla = () => {
    if (operador) {
        operacionElement.textContent = `${valorAnterior} ${operador} ${valorActual}`;
    } else {
        operacionElement.textContent = valorActual || "0";
    }
    resultadoElement.textContent = valorActual || valorAnterior || "0";
};

// Función para manejar la evaluación de la operación
const calcularResultado = () => {
    try {
        let expresion = `${valorAnterior || 0}${operador}${valorActual || 0}`;
        expresion = expresion.replace(/--/g, '+');

        // Evaluar la expresión
        const resultado = eval(expresion);

        // Manejar el caso de la división por cero
        if (resultado === Infinity || resultado === -Infinity) {
            // Deshabilitar todos los botones excepto "C"
            botones.forEach((boton) => {
                boton.disabled = boton.dataset.value !== 'C';
            });
            return "División por cero";
        } else {
            // Habilitar todos los botones
            botones.forEach((boton) => {
                boton.disabled = false;
            });
            return resultado;
        }
    } catch (error) {
        // Deshabilitar todos los botones excepto "C"
        botones.forEach((boton) => {
            boton.disabled = boton.dataset.value !== 'C';
        });
        return "Error";
    }
};

// Función para manejar el clic en un botón
const manejarClickBoton = (valor) => {
    // Si el valor actual es algún "Error", no permitir ninguna operación excepto "C"
    if (resultadoElement.innerText === "Error" || resultadoElement.innerText === "División por cero") {
        if (valor !== "C") {
            return; // No hacer nada si no se presiona "C"
        } else {
            // Si se presiona "C", desbloquear todos los botones
            botones.forEach((boton) => {
                boton.disabled = false;
            });
        }
    }

    // Si es un número o un punto decimal
    if (!isNaN(Number(valor)) || valor === ".") {
        if (resultadoMostrado) {
            valorActual = valor === "." ? "0." : valor;
            resultadoMostrado = false;
        } else {
            if (valorActual === "0" && valor !== ".") {
                valorActual = valor;
            } else {
                valorActual += valor;
            }
        }
    }

    // Función de potenciación (x²)
    else if (valor === "^") {
        if (valorActual) {
            valorActual = Math.pow(parseFloat(valorActual), 2).toString();
            resultadoMostrado = true;
        }
    }
    // Función de raíz cuadrada (√)
    else if (valor === "√") {
        if (valorActual) {
            valorActual = Math.sqrt(parseFloat(valorActual)).toString();
            resultadoMostrado = true;
        }
    }
    // Función de porcentaje (%)
    else if (valor === "%") {
        if (valorActual) {
            valorActual = (parseFloat(valorActual) / 100).toString();
            resultadoMostrado = true;
        }
    }
    // Cambiar signo del número (±)
    else if (valor === "±") {
        if (valorActual) {
            valorActual = (parseFloat(valorActual) * -1).toString();
        } else if (operador) {
            valorAnterior = (parseFloat(valorAnterior) * -1).toString();
        }
    }
    // Si se quiere limpiar la calculadora
    else if (valor === "C") {
        valorActual = "";
        valorAnterior = "";
        operador = null;
        resultadoMostrado = false;
    }
    // Si se presiona un operador (+, -, *, /)
    else if (["+", "-", "*", "/"].includes(valor)) {
        if (valorActual) {
            if (valorAnterior === "Error") {
                valorAnterior = valorActual;
            } else if (valorAnterior && operador) {
                valorAnterior = calcularResultado().toString();
            } else {
                valorAnterior = valorActual;
            }
            valorActual = "";
            operador = valor;
            resultadoMostrado = false;
        }
    }
    // Si se presiona el botón de igual
    else if (valor === "=" && valorAnterior && operador && valorActual) {
        const resultadoFinal = calcularResultado().toString();
        operacionElement.textContent = `${valorAnterior} ${operador} ${valorActual} =`;
        valorActual = resultadoFinal;
        valorAnterior = "";
        operador = null;
        resultadoMostrado = true;
    }
    actualizarPantalla();
};
