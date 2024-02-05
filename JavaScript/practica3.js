function calculoNumero(){
    var numero = parseFloat(document.getElementById('numero').value);
    if (!isNaN(numero)) {
        if (numero > 0) {
            document.getElementById('resultado').textContent = 'Positivo';
        }
        if (numero < 0 ) {
            document.getElementById('resultado').textContent = 'Negativo';
        }
        if (numero == 0) {
            document.getElementById('resultado').textContent = 'Es numero es Cero';
        }
    } else {
        document.getElementById('resultado').textContent = 'Ingrese un valor valido';
    }
}