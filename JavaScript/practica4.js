function ImprimirNumeros(){
    let element = [];
    for (let index = 0; index < 11; index++) {
        element[index] = index;
    }
    document.getElementById('resultado').textContent = element;
    
}