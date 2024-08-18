"use strict";
// Seleccionar los elementos HTML
const resultado = document.getElementById("resultado");
const botones = document.querySelectorAll(".boton");
const operacionSpan = document.getElementById("operacion");

// Variables para guardar los estados
let valorActual = "";
let valorAnterior = "";
let operador = null;

// Asignar el evento click a cada botón
botones.forEach((boton) => {
    boton.addEventListener("click", () => {
        const valor = boton.getAttribute("data-value");
        manejarClickBoton(valor);
    });
});

// Función para actualizar el resultado
const actualizarResultado = (valor) => {
    resultado.innerHTML = `<span id="operacion">${operacionSpan.innerHTML}</span> ${valor}`;
};

// Función para actualizar el span de operación
const actualizarSpanOperacion = () => {
    if (operador) {
        operacionSpan.innerHTML = `${valorAnterior} ${operador} ${valorActual}`;
    } else {
        operacionSpan.innerHTML = `${valorActual}`;
    }
};

// Función para manejar la evaluación de la operación
const calcularResultado = () => {
    let resultadoOperacion;
    try {
        if (operador === "/" && valorActual === "0") {
            throw "División por cero";
        }
        resultadoOperacion = eval(`${valorAnterior}${operador}${valorActual}`);
    } catch (error) {
        resultadoOperacion = "Error";
    }
    return resultadoOperacion;
};

// Función para manejar el clic en un botón
const manejarClickBoton = (valor) => {
    // Si es un número o un punto decimal
    if (!isNaN(Number(valor)) || valor === ".") {
        // Evitar ceros a la izquierda
        if (valorActual === "0" && valor !== ".") {
            // Reemplaza "0" por el valor ingresado
            valorActual = valor;
        } else {
            valorActual += valor;
        }
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
        if (valorActual === "")
            return;
        // Si hay un operador y un valor anterior, realizar la operación actual
        if (operador && valorAnterior) {
            const resultadoOperacion = calcularResultado();
            valorAnterior = resultadoOperacion.toString();
            actualizarResultado(resultadoOperacion.toString());
            operacionSpan.innerHTML = `${valorAnterior}${operador}`;
        } else {
            valorAnterior = valorActual;
        }
        valorActual = "";
        operador = valor;
        actualizarSpanOperacion();
    }
    // Si se presiona el botón de igual
    else if (valor === "=") {
        if (valorAnterior && operador && valorActual) {
            const resultadoOperacion = calcularResultado();
            valorAnterior = resultadoOperacion.toString();
            valorActual = "";
            operador = null;
            operacionSpan.innerHTML = `${valorAnterior}`; // Mostrar el resultado en el span de operación
            actualizarResultado(valorAnterior);
        }
    }
};