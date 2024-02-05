// declara variables e imprime resultado 
// OP 1:

// let numero1 = 3; 
// let numero2 = 3;
// let suma = numero1+numero2;
// document.write(suma);

// OP 2

function CalculoSuma(){
    var valor1 = parseFloat(document.getElementById('valor1').value);
    var valor2 = parseFloat(document.getElementById('valor2').value);

    if (!isNaN(valor1) && !isNaN(valor2)) {
        var resultadoSuma = valor1+valor2;
        document.getElementById('resultado').textContent = 'La suma es: ' + resultadoSuma;
    }else{
        document.getElementById('resultado').textContent = 'Ingrese valores validos';
    }
}
