document.addEventListener('DOMContentLoaded', ()=> {
    console.log(location.protocol + '//' + document.domain + ':' + location.port);
    //Conecta ao websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    //Quando conectado, configura os botões
    socket.on('connect', () => {

        // Cada botão deve mandar um evento de "submit voto"
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {                
                const selecionado = button.dataset.voto;
                socket.emit('FuncVoto', {'selecionado': selecionado});
            };
        });
    });

    // Quando um novo voto é realizado, adiciona na lista não ordenada
    socket.on('Func_Voto', data => {
        document.querySelector('#sim').innerHTML = data.sim;
        document.querySelector('#nao').innerHTML = data.nao;
        document.querySelector('#talvez').innerHTML = data.talvez;
    })
});