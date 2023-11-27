function listagem_generica(Jogador, jogadores, id, nome, macas_coletadas) {

    // chamada ao backend
    var rota = `http://localhost:5000/listar/${Jogador}`;

    // chamada ajax
    var acao = $.ajax({
        url: rota,
        dataType: 'json', // os dados são recebidos no formato json,
    });

    // se a chamada der certo
    acao.done(function (retorno) {
        // faz uma proteção contra erros
        try {
            if (retorno.resultado == "ok") {
                // percorrer a lista de pessoas retornadas; 
                for (var reg of retorno.detalhes) { //p vai valer cada pessoa do vetor de pessoas
                    // criar um parágrafo
                    var paragrafo = $(elemento_html);
                    // informar o HTML deste parágrafo
                    // observe o apóstrofo inclinado, para interpretar as variáveis
                    //paragrafo.html(`==> ${p.nome}, ${p.email}`);
                    var s = '';
                    for (campo of lista_campos) {
                        // os campos pode ser acessados como
                        // reg.campo
                        // ou
                        // reg[campo]
                        // ***** se for um campo composto, estará descrito como, por exemplo: pessoa.nome
                        // obs: só suporta 1 ponto até o momento

                        // se tem "." no campo, precisa fazer o parse
                        var teste = String(campo);
                        if (teste.indexOf(".") !== -1) {
                            // faz o parse
                            var partes = teste.split(".");
                            // pega o valor usando campo1.campo2
                            var valor = reg[partes[0]][partes[1]];
                            // o valor não está definido? Deu problema?
                            if (valor == undefined) {
                                valor = "";
                            }
                            s = s + html_antes + valor + html_depois;
                        } else {
                            s = s + html_antes + reg[campo] + html_depois;
                        }
                    }
                    paragrafo.html(`${s}`);
                    // adicionar o parágrafo criado na div
                    $('#' + jogadores).append(paragrafo);
                }
            } else {
                alert("Erro informado pelo backend: " + retorno.detalhes);
            }
        } catch (error) { // se algo der errado...
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno.detalhes);
        }
    });

    // se a chamada der erro
    acao.fail(function (jqXHR, textStatus) {
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });
}

// função para encontrar o erro
// https://stackoverflow.com/questions/6792878/jquery-ajax-error-function 
function encontrarErro(jqXHR, textStatus, rota) {
    var msg = '';
    if (jqXHR.status === 0) {
        msg = 'Não foi possível conectar, ' +
            'verifique se o endereço do backend está certo' +
            ' e se o backend está rodando.';
    } else if (jqXHR.status == 404) {
        msg = 'A URL informada não foi encontrada no ' +
            'servidor [erro 404]: ' + rota;
    } else if (jqXHR.status == 500) {
        msg = 'Erro interno do servidor [erro 500], ' +
            'verifique nos logs do servidor';
    } else if (textStatus === 'parsererror') {
        msg = 'Falha ao decodificar o resultado json';
    } else if (textStatus === 'timeout') {
        msg = 'Tempo excessivo de conexão, estourou o limite (timeout)';
    } else if (textStatus === 'abort') {
        msg = 'Requisição abortada (abort)';
    } else {
        msg = 'Erro desconhecido: ' + jqXHR.responseText;
    }
    return msg;
}
