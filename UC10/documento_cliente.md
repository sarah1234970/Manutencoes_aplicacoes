Cenário: Sistema de registro de clientes que foi programado com vários bugs

Recursos para testa:

Campos de entrada do usuário (por exemplo, nome, e-mail, senha)
Processo de submissão
Mensagens de erro e validações
Experiência geral do usuário
Bug Hunting
Atiivdade-

5 problemas diferentes no sistema de registro de clientes.

1- erro
Quando entra no modo de edição do perfil do cliente, ao finalizar os ajustes das informações, ao invés de atualizar os dados, ele duplica o cliente, resutando em dois cadastros do mesmo usuário.

    const cliente = {
        id: nextId++,
        nome: nome,
        email: email,
        cpf: cpf,
        telefone: telefone,
        cidade: cidade,
        status: status,
        dataCadastro: new Date().toLocaleDateString()
        };
        clientes.push(cliente);
        showMessage('✅ Cliente cadastrado com sucesso!', 'success');
        atualizarListaClientes();
        limparFormulario();

Toda vez que esse código é executado seja para um novo cadastro ou após clicar em "Editar" a lógica de edição (IF/ELSE) está ausente.

Correção:

        let clientes = [];
        let nextId = 1;
        let editingID = null; // variável para rastrear o cliente em edição

- Agora temos uma variável para rastrear o cliente em edição

            if (editingID) { // agora sim, atualiza o cliente existente
                const cliente = clientes.find(c => c.id === editingID);
                if (cliente) {
                    cliente.nome = nome;
                    cliente.email = email;
                    cliente.cpf = cpf;
                    cliente.telefone = telefone;
                    cliente.cidade = cidade;
                    cliente.status = status;
                    showMessage('✅ Cliente atualizado com sucesso!', 'success');

                    editingID = null; // resetar o ID de edição
                }
- Agora tem a atualização dos dados que não duplica o perfil cadastrado


                function editarCliente(id) {
                    const cliente = clientes.find(c => c.id === id);
                    if (cliente) {
                        editingID = id; // definir o ID do cliente em edição
                        document.getElementById('nome').value = cliente.nome;
                        document.getElementById('email').value = cliente.email;
                        document.getElementById('cpf').value = cliente.cpf;
                        document.getElementById('telefone').value = cliente.telefone || '';
                        document.getElementById('cidade').value = cliente.cidade || '';
                        document.getElementById('status').value = cliente.status;
                        showMessage('Você está editando um cliente!✏️', 'success');  
                    }
                }

- Agora o sistema identifica o id do cliente que está digitando

                function limparFormulario() {
                    document.getElementById('clientForm').reset();
                    document.getElementById('message').innerHTML = '';
                    editingID = null; // resetar o ID de edição ao limpar o formulário // aqui ele identifica
                    showMessage('🧹 Formulário limpo!', 'success');
                }
- Sistema notifica que o formulário em edição foi limpo

2- erro ** 
quando o usuário digita o cpf ele não exige limite de número, ou seja, o usuário pode adicionar mais números ou menos, mas o cpf tem uma quantidade de números padrão

            <div class="form-group">
                <label for="cpf">CPF *</label>
                <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required > 
                <small>Formato: 000.000.000-00</small>
            </div>
correção:

    <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required pattern="\d{3}\.\d{3}\.\d{3}-\d{2}">

3- erro
Ao clicar no botão de cadastrar clientes após informações salvas o sistema não avisa que as informações foram alteradas


4- erro ** 
Ao informar o telefone, ele não exige limite de número, ou seja o usuário pode adicionar mais números ou menos, mas o telefone tem uma quantidade de números padrão

    <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000">
                
Correção:

    <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">

5- erro 
Ao clicar no botão de limpar os campos, o sistema não mostra uma mensagem que avisa que os campos foram limpos

6- erro 
Ao clicar no botão de cadastrar cliente o sistema não mostra uma mensagem notificando que o usuário foi cadastrado


7- erro 
O sistema mostra uma mensagem informando que está no modo de edição como uma mensagem de alerta

    {
    showMessage('⚠️ Modo edição - cuidado com duplicatas!', 'error'); // aviso de edição está como error 
    }
O "showMessage" estava apresentando como erro o modo de edição 

Correção:

    {
    showMessage('Você está editando um cliente!✏️', 'success'); // aviso de edição está como error 
    }
Agora ele apresenta um campo válido, informando que o usuário está editando um cliente, sem gerar erros

8- erro 
Não tem uma ação de botão para cancelar a edição


9- erro ** 
Não mostra um exemplo de formato do telefone em relação aos outros campos como: cpf, e-mail e nome

        <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000">
    </div>

Correção:

    <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
        <small>Formato: (00) 00000-0000</small>
    </div>

10- Falha 
Em clientes cadastrados, não infoma quando ouve a última atualização de dados caso o cliente tenha editado as informações por exemplo

11- erro 
No campo de telefone onde deveria ser apenas números o campo permite letras

    <input type="text" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">

O type está selecionando como "text", permitindo letras

Correção:

    <input type="number" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
    

O type agora seleciona "number", ou seja, vai aceitar apenas números

12- erro 
No campo de CPF onde deveria ser apenas números o campo permite letras

    <input type="number" id="cpf" name="cpf" placeholder="000.000.000-00" required pattern="\d{3}\.\d{3}\.\d{3}-\d{2}">

13- Ao cadastrar novos clientes, caso seja adicionado as mesmas informações de um usuário já cadastrado, o sistema aceita gerando duplicatas de um cadastro novo de um usuário existente

    function verificarClienteExistente(email, cpf) {
        return false;
    }

Atualmente, essa função está retornando sempre false, o que permite a duplicação das informações existentes.

Correção:



    function verificarClienteExistente(email, cpf) {
            return clientes.some(cliente => cliente.email === email || cliente.cpf === cpf);
        }

Ao invés de retornar falso, agora retorna "cliente.some" se some() retorna verdadeiro, significa que um cliente duplicado foi encontrado, no sentido de alguém = some. Agora quando isso acontecer vai retornar essa mensagem:

    if (verificarClienteExistente(email, cpf)) {
    showMessage('❌ Cliente já cadastrado!', 'error'); // Essa mensagem será exibida
    return; // O cadastro é interrompido aqui}







erro: ação ou equivoco do programador (lógica do código)

falha: quando voce não esperava que acontecesse

bug: tras resultados incorretos (o sistema não funciona)
