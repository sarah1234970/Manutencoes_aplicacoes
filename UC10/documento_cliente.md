Cenário: Sistema de registro de clientes que foi programado com vários bugs

Recursos para testa:

Campos de entrada do usuário (por exemplo, nome, e-mail, senha)
Processo de submissão
Mensagens de erro e validações
Experiência geral do usuário
Bug Hunting
Atiivdade-

5 problemas diferentes no sistema de registro de clientes.

1- erro Quando entra no modo de edição ele adiciona duplicatas ao invés de informar que as informações escritas ja foram adicionadas.

2- erro ** quando o usuário digita o cpf ele não exige limite de número, ou seja o usuário pode adicionar mais números ou menos, mas o cpf tem uma quantidade de números padrão

            <div class="form-group">
                <label for="cpf">CPF *</label>
                <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required > 
                <small>Formato: 000.000.000-00</small>
            </div>
correção:

            <div class="form-group">
                <label for="cpf">CPF *</label>
                <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required pattern="\d{3}\.\d{3}\.\d{3}-\d{2}">
                <small>Formato: 000.000.000-00</small>
            </div>
3- erro Ao clicar no botão de cadastrar clientes após informações salvas o sistema não avisa que as informações foram alteradas

4- erro ** ao informar o telefone ele não exige limite de número, ou seja o usuário pode adicionar mais números ou menos, mas o telefone tem uma quantidade de números padrão

            <div class="form-group">
                <label for="telefone">Telefone</label>
                <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000">
                <small>Formato: (00) 00000-0000</small>
            </div>
correção:

            <div class="form-group">
                <label for="telefone">Telefone</label>
                <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
                <small>Formato: (00) 00000-0000</small>
            </div>
5- erro ao clicar no botão de limpar os campos o sistema não mostra uma mensagem que avisa que os campos foram limpos

6- erro ao clicar no botão de cadastrar cliente o sistema não mostra uma mensagem notificando que o usuário foi cadastrado

7- erro o sistema mostra uma mensagem informando que está no modo de edição como uma mensagem de alerta e desaparece em poucos segundos

                  {
                showMessage('⚠️ Modo edição - cuidado com duplicatas!', 'error'); // aviso de edição está como error 
            }
O showMessage estava apresentando como erro o modo de edição correção:

                  {
                showMessage('Você está editando um cliente!✏️', 'success'); // aviso de edição está como error 
            }
Agora ele apresenta um campo válido informando que o usuário está editando um cliente, sem gerar erros

8- erro não tem uma ação de botão para cancelar a edição

9- erro ** não mostra um exemplo de formato do telefone em relação aos outros campos como: cpf, e-mail e nome

            <div class="form-group">
                <label for="telefone">Telefone</label>
                <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000">
            </div>
correção:

            <div class="form-group">
                <label for="telefone">Telefone</label>
                <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
                <small>Formato: (00) 00000-0000</small>
            </div>
10- erro em clientes cadastrados não infoma quando ouve a última atualização de dados caso o cliente tenha editado as informações por exemplo

11- erro no campo de telefone onde deveria ser apenas números o campo permite letras

<input type="text" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
o type está selecionando como texto, permitindo letras

correção:

<input type="number" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
o type agora seleciona number, ou seja, vai aceitar apenas números

11- erro no campo de CPF onde deveria ser apenas números o campo permite letras

12- Ao cadastrar novos clientes, caso seja adicionado as mesmas informações de um usuário já cadastrado, o sistema aceita gerando duplicatas de um cadastro novo de um usuário existente

    function verificarClienteExistente(email, cpf) {
        return false;
    }
Atualmente, essa função está retornando sempre false, o que permite a duplicação das informações existentes.

correção:

@param {string} email - O e-mail a ser verificado.
@param {string} cpf - O CPF a ser verificado.
@returns {boolean} - Retorna true se um cliente duplicado for encontrado, false caso contrário. */ function verificarClienteExistente(email, cpf) { // A função 'some' verifica se pelo menos um elemento (cliente) // no array 'clientes' satisfaz a condição (email OU cpf são iguais). return clientes.some(cliente => cliente.email === email || cliente.cpf === cpf ); }
erro: ação ou equivoco do programador (lógica do código)

falha: quando voce não esperava que acontecesse

bug: tras resultados incorretos (o sistema não funciona)
