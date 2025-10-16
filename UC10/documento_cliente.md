Cenário: Sistema de registro de clientes que foi programado com vários bugs

Recursos para testa:

- Campos de entrada do usuário (por exemplo, nome, e-mail, senha)
- Processo de submissão
- Mensagens de erro e validações
- Experiência geral do usuário

### Bug Hunting

Atiivdade- 

5 problemas diferentes no sistema de registro de clientes.

1- erro

Quando entra no modo de edição ele adiciona duplicatas ao invés de informar que as informações escritas ja foram adicionadas.

2- erro 

quando o usuário digita o cpf ele não exige limite de número, ou seja o usuário pode adicionar mais números ou menos, mas o cpf tem uma quantidade de números padrão

3-  erro

 Ao clicar no botão de cadastrar clientes após informações salvas o sistema não avisa que as informações foram alteradas

4- erro 

ao informar o telefone ele não exige limite de número, ou seja o usuário pode adicionar mais números ou menos, mas o telefone tem uma quantidade de números padrão

5- erro

ao clicar no botão de limpar os campos o sistema não mostra uma mensagem que avisa que os campos foram limpos

6- erro 

ao clicar no botão de cadastrar cliente o sistema não mostra uma mensagem notificando que o usuário foi cadastrado

7- erro 

o sistema mostra uma mensagem  informando que está no modo de edição como uma mensagem de alerta e desaparece em poucos segundos

8- erro

não tem uma ação de botão para cancelar a edição

9-  erro

não mostra um exemplo de formato do telefone em relação aos outros campos como: cpf, e-mail e nome

10- erro 

em clientes cadastrados não infoma quando ouve a última atualização de dados caso o cliente tenha editado as informações por exemplo

erro: ação ou equivoco do programador (lógica do código)

falha: quando voce não esperava que acontecesse 

bug: tras resultados incorretos (o sistema não funciona)
