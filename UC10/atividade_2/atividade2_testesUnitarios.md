## **Aula 2: Classificação de Falhas e Preparação para Testes Unitários**

---

# Classificação de Falhas e Preparação para Testes Unitários 📰

**Objetivo:** Consolidar os conceitos fundamentais de teste de software e classificá-los, aprofundando a documentação das falhas encontradas na Aula 1.

---

## **Bloco 1: Ação - Formalizando os Conceitos 📚**

 **Pesquisa Individual e Glossário**

- **DEFEITO (Bug/Defect):**

**O que é?**

O defeito é como se fosse um “bug” ele é causado no período de desenvolvimento do software, quando um código é inserido de forma errada no processo de criação. 

**Onde ele está?**

Um defeito pode se manifestar de várias formas, desde um cálculo incorreto até uma funcionalidade que não está operando conforme as regras. É importante ressaltar que um defeito não é necessariamente percebido imediatamente após sua introdução no código, ele pode permanecer até ser ativado por certas condições durante a execução do programa.

- **ERRO (Mistake/Error):**

**O que é?**

O erro seria um resultado do defeito. É quando executamos algo e recebemos uma resposta equivocada. Esses erros podem ser introduzidos em várias etapas do processo de desenvolvimento, desde o entendimento até a implementação do código.

 **Quem o comete?**

Um erro pode ocorrer quando um desenvolvedor comete um equívoco na codificação, como uma sintaxe incorreta ou uma lógica inadequada.

- **FALHA (Failure):**

**O que é?** 

É quando um software apresenta comportamento e respostas diferentes do que é esperado. É um comportamento inconsistente do sistema.  É o momento em que o sistema não atende às expectativas do usuário ou não realiza suas funções conforme o esperado.

**O que o usuário vê?**

uma falha pode ocorrer quando um botão de "enviar" em um aplicativo de e-mail não executa a ação de enviar a mensagem. 

---

**Melhor Prática:** Pense no **Sistema de Cadastro de Clientes** que você testou. Se o CPF 111.111.111-11 for aceito:

- **Defeito:** É a falta de lógica no código JavaScript (validarCPF).
- **Erro:** Foi a omissão do desenvolvedor que esqueceu de implementar a validação completa.
- **Falha:** É o cliente ser cadastrado com um CPF inválido, comprometendo o sistema.

Resposta: 
**Falha** - o CPF `111.111.111-11` **é uma falha**, pois o erro do programador,  gerou um defeito no código que se manifestou no comportamento incorreto do sistema.

---

### Classificação das Falhas

| **Situação (Descrição)** | **Classificação**  | **Defeito (no Código)** | **Erro (Humano)** | **(Comportamento)** |
| --- | --- | --- | --- | --- |
| **1.** Sistema duplicava cliente ao tentar editar cadastro | Erro | Lógica de edição ausente (`editingID` era `null`) | Falha na Lógica (Ausência de identificação para edição) | Cliente duplicado na lista após tentativa de edição |
| **2.** Campo de CPF permitia qualquer número de dígitos | Erro | Ausência de validação de formato/padrão (tipo `text` sem `pattern`) | Falha no Requisito/Lógica de Programação (Tipo de campo incorreto, falta de `pattern`) | Sistema aceita e insere CPF com formato inválido |
| **3.** Após salvar alterações, o sistema não exibia notificação | Falha | Código para exibição de mensagem de sucesso ausente | Falha no Requisito (Ausência de feedback visual) | Usuário não recebe confirmação visual de atualização |
| **4.** Campo telefone permitia qualquer número de dígitos | Erro | Ausência de validação de formato/padrão (tipo `text` sem `pattern`) | Falha no Requisito/Lógica de Programação (Falta de validação de caracteres/dígitos) | Sistema aceita e insere telefone com formato inválido |
| **5.** Botão “Limpar” não informava que o formulário foi limpo | Falha | Código para exibição de mensagem de limpeza ausente | Falha no Requisito (Ausência de feedback visual) | Formulário limpa sem notificar o usuário |
| **6.** Ao cadastrar cliente, o sistema não mostrava notificação | Falha | Código para exibição de mensagem de sucesso de cadastro ausente | Falha no Requisito (Ausência de mensagem de validação) | Cadastro é concluído sem notificação de sucesso |
| **7.** Alerta de edição aparecia como erro visual | Erro | Classificação visual de mensagem errada (`'error'` em vez de `'success'`) | Falha na Lógica de Programação (Uso incorreto da categoria visual de feedback) | Mensagem de edição é exibida com aparência de erro |
| **8.** Ausência de botão para cancelar edição | Erro | Elemento HTML e função de cancelamento ausentes | Falha no Requisito (Impossibilidade de sair do modo de edição sem atualizar) | Usuário fica preso no modo de edição |
| **9.** Campo telefone não mostrava exemplo de formato | Falha | Elemento `<small>` com indicação de formato ausente | Falha no Requisito (Falta de instrução visual para o usuário) | Usuário não tem referência visual para o formato de telefone esperado |
| **10.** Sistema não informava data de atualização de cadastro | Falha | Lógica para armazenar e exibir `dataAtualizacao` ausente | Falha no Requisito (Falta de controle de histórico de atualizações) | Informação de quando o cadastro foi atualizado não é exibida |
| **11.** Campo telefone permitia letras | Erro | Tipo de input era `text` | Falha no Requisito/Lógica de Programação (Permissão de caracteres não numéricos) | Caracteres não numéricos são aceitos no campo de telefone |
| **12.** Campo CPF permitia letras | Erro | Tipo de input era `text` | Falha no Requisito/Lógica de Programação (Não restringia entrada numérica) | Caracteres não numéricos são aceitos no campo de CPF |
| **13.** Sistema permitia cadastro duplicado (mesmo e-mail/CPF) | Defeito | A função `verificarClienteExistente` retornava sempre `false` | Falha na Lógica de Programação (Função de verificação não implementada corretamente) | Cadastro duplicado (mesmo e-mail/CPF) é inserido na lista |

---

## **Bloco 2: Reflexão - Preparando o Teste Unitário 📑**

### **Análise e Separação de Módulos**

1. **Unitário vs. Sistema:**

- Essas funções que só verificam apenas um valor são úteis para o teste unitário, pois elas verificam somente um valor.
- O clique no botão **Cadastrar** é bom para um Teste de Sistema (também conhecido como Teste e*nd-to-end* (ponta a ponta) porque ele envolve a **interação de múltiplos componentes** e verifica o **sistema em geral.**
1. **Particionamento de Equivalência (Teoria):**

Essa teoria sugere que ao invés de testar todos as possibilidades de valores de entrada, seja **divido** todos esses valores em grupos ou classes, onde se estima que todos os membros de uma classe se comportarão do mesmo jeito.

- Se um único valor da classe **válida** funcionar, presume-se que todos os outros valores válidos também funcionarão.
- Se um único valor da classe **inválida** falhar, presume-se que todos os outros valores também falharam.
- Exemplo de 3 classes de entrada de dados:

| **Classe de Equivalência** | **Exemplo de Entrada** | **Justificativa** | **Resultado Esperado (True/False)** |
| --- | --- | --- | --- |
| **Válida** (Formato normal) | `sarah.d@edu.com.br` | Entrada com um prefixo, um `@`, um domínio e um TLD (Top-Level Domain) padrão. | **True** |
| **Inválida** (Sem TLD) | `nome@dominio` | Entrada que falha ao incluir o domínio de nível superior (como `.com` ou `.br`). | **False** |
| **Inválida** (Espaços em Branco) | `" teste@dominio.com "` | Entrada que pode falhar em uma validação, pois os espaços do início ou no fim (que devem ser rejeitados ou removidos antes de validar). | **False** |
- **Testes Unitários** para verificar a lógica
- **Testes de Sistema** para verificar a **integração** e o **comportamento** do sistema

---

## **Bloco 3: Nova Ação - Modelando Casos de Teste Unitário 🛠💻**

### **Criação de 5 Casos de Teste Unitário**

| Nome do Teste | Pré-Condições | Passos para Executar | Resultado Esperado | Tipo de Teste |
| --- | --- | --- | --- | --- |
| CTU-001: CPF Válido - Padronizado | Nenhuma | Chamar a função validarCPFCompleto('97059719069 | True | Unitário |
| CTU-002: Digitos Repetidos | Nenhuma | Chamar a função de “validarCPFCompleto(’11111111111’)” | False | Unitário |
| CTU-003: CPF com 10 dígitos | Nenhuma | Chamar a função validarCPFCompleto('1234567890') | False | Unitário |
| CTU-004: CPF com Letras | Nenhuma | **Chamar a função validarCPFCompleto('970.59A.190-69')** | False | Unitário |
| CTU-005: CPF Vazio | Nenhuma | Chamar função validarCPFCompleto(’ ’) | False | Unitário |

---

**Aula 2: Classificação de Falhas e Preparação para Testes Unitários**

**Atividade remota**

---

Agradeço pela leitura e analise da atividade!

Por: Sarah Dyovanna

Turma: 211

Unidade Curricular - UC10: Realizar testes nas aplicações desenvolvidas
