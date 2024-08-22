"use strict";

// Seleccionar los elementos HTML
const resultadoElement = document.getElementById("resultado");
const operacionElement = document.getElementById("operacion");
const botones = document.querySelectorAll(".boton");

// Variables para guardar los estados
let valorActual = "";
let valorAnterior = "";
let operador = null;
let resultadoMostrado = false;  // Nueva variable para rastrear si se mostró un resultado

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
        // Verificar si se está realizando una división por cero
        if (operador === "/" && valorActual === "0") {
            throw new Error("División por cero");
        }
        return eval(`${valorAnterior}${operador}${valorActual}`);
    } catch (error) {
        return "Error"; // Si ocurre un error, retornar "Error"
    }
};

// Función para manejar el clic en un botón
const manejarClickBoton = (valor) => {
    // Si el valor actual es "Error", no permitir ninguna operación excepto "C"
    if (valorActual === "Error") {
        if (valor !== "C") {
            return;
        }
    }

    // Si es un número o un punto decimal
    if (!isNaN(Number(valor)) || valor === ".") {
        if (resultadoMostrado) {
            // Si se muestra un resultado, al presionar un número se reinicia la calculadora
            valorActual = valor === "." ? "0." : valor;
            resultadoMostrado = false;
        } else {
            if (valorActual === "0" && valor !== ".") {
                valorActual = valor; // Reemplaza "0" por el valor ingresado
            } else {
                valorActual += valor;
            }
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
        if (valorActual && valorActual) {
            if (valorAnterior === "Error") {
                valorAnterior = valorActual;
            } else if (valorAnterior && operador) {
                valorAnterior = calcularResultado().toString();
                console.log(`Valor anterior: ${valorAnterior}, ${operador}, ${valorActual}`);
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
        resultadoMostrado = true;  // Indica que se mostró un resultado
    }
    actualizarPantalla();
};
