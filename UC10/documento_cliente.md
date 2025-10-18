# 🧾 Relatório Padronizado de Correções – Sistema de Cadastro de Clientes

## Contexto

O sistema original (`antigo.html`) apresentava vários problemas, validação e experiência do usuário.

Após análise de testes foram identificadas **13 situações** de erro, falha e defeito.

Este relatório descreve cada uma delas com seus  trechos corrigidos e justificativas.

---

## **1. Situação:** Sistema duplicava cliente ao tentar editar cadastro📋

**Classificação:** Erro

**Justificativa:** O código não tinha identificação para edição (`editingID`), o que fazia o sistema cadastrar um novo cliente em vez de atualizar o existente.

**Trecho original** 

```jsx
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

```

**Trecho corrigido**

```jsx
if (editingID === null) {
    const cliente = { id: nextId++, nome, email, cpf, telefone, cidade, status, dataCadastro: new Date().toLocaleDateString() };
    clientes.push(cliente);
} else {
    const cliente = clientes.find(c => c.id === editingID);
    if (cliente) {
        cliente.nome = nome;
        cliente.email = email;
        cliente.cpf = cpf;
        cliente.telefone = telefone || '';
        cliente.cidade = cidade || '';
        cliente.status = status;
    }
    editingID = null;
}

```

**Descrição técnica:**

Implementação da variável `editingID` para localizar o cliente em edição, impedindo duplicações. A lógica `if/else` diferencia cadastro e atualização.

---

## **2. Situação:** Campo de CPF permitia qualquer número de dígitos. 🔢

**Classificação:** Erro

**Justificativa:** O campo não possuía um padrão de formato, ou seja, permitia letras e símbolos que não fazem parte da padronização.

**Trecho original:**

```html
<input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>

```

**Trecho corrigido :**

```html
<input type="number" id="cpf" name="cpf" placeholder="000.000.000-00" required pattern="\d{3}\.\d{3}\.\d{3}-\d{2}">

```

**Descrição técnica:**

Adição do atributo `pattern` com regex e substituição do tipo para `number`, restringindo o formato aceito do CPF.

---

## **3. Situação:** Após salvar alterações, o sistema não exibia notificação. 💬

**Classificação:** Falha

**Justificativa:** O usuário não recebia feedback visual após editar informações.

**Trecho original** 

```jsx
                document.getElementById('status').value = cliente.status;
                showMessage('⚠️ Modo edição - cuidado com duplicatas!', 'error');
            }
        }
// não havia mensagem para atualização

```

**Trecho corrigido** 

```jsx
showMessage('✅ Cliente atualizado com sucesso!', 'success');

```

**Descrição técnica:**

Foi adicionada a mensagem de sucesso após atualização para indicar que o processo ocorreu corretamente.

---

## **4. Situação:** Campo telefone permitia qualquer número de dígitos. ☎️

**Classificação:** Erro

**Justificativa:** O campo não validava o número de caracteres, ou seja, permitia letras e símbolos que não fazem parte da padronização.

**Trecho original**

```html
<input type="text" id="telefone" name="telefone" placeholder="(00) 00000-0000">

```

**Trecho corrigido**

```html
<input type="number" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">

```

**Descrição técnica:**

A inclusão do `pattern` e ajuste do tipo `number` vão garantir que apenas números sejam incluídos.

---

## **5. Situação:** Botão “Limpar” não informava que o formulário foi limpo.

**Classificação:** Falha

**Justificativa:** A ação era executada, mas não havia mensagem visual indicando a ação.

**Trecho original** 

```jsx
function limparFormulario() {
    document.getElementById('clientForm').reset();
    document.getElementById('message').innerHTML = '';
}

```

**Trecho corrigido**

```jsx
function limparFormulario() {
    document.getElementById('clientForm').reset();
    document.getElementById('message').innerHTML = '';
    editingID = null;
    showMessage('🧹 Formulário limpo!', 'success');
}

```

**Descrição técnica:**

Adição de mensagem de confirmação ao usuário e redefinição do `editingID` para editar as info.

---

## **6. Situação:** Ao cadastrar cliente, o sistema não mostrava notificação de cadastro adicionado. ✅

**Classificação:** Falha

**Justificativa:** O cadastro era feito, mas o usuário não tinha uma mensagem validando .

**Trecho original** 

```jsx
						clientes.push(cliente);
            atualizarListaClientes();
            limparFormulario();
        });

```

**Trecho corrigido**

```jsx
						clientes.push(cliente);
            showMessage('✅ Cliente cadastrado com sucesso!', 'success');
            atualizarListaClientes();
            limparFormulario();
        });

```

**Descrição técnica:**

Adição de notificação do usuário adicionado, para melhor visualização de confirmação.

---

## **7. Situação:** Alerta de edição aparecia como erro visual. ⚠️

**Classificação:** Erro

**Justificativa:** A mensagem “modo edição” estava sendo tratada como erro (`'error'`), confundindo o usuário.

**Trecho original** 

```jsx
showMessage('⚠️ Modo edição - cuidado com duplicatas!', 'error');

```

**Trecho corrigido**

```jsx
showMessage('Você está editando um cliente!✏️', 'success');

```

**Descrição técnica:**

Correção da categoria visual de mensagem e reformulação do texto para feedback positivo.

---

## **8. Situação:** Ausência de botão para cancelar edição. ✖️

**Classificação:** Erro

**Justificativa:** O usuário não podia sair do modo de edição **sem atualizar dados**.

**Trecho original** 

```jsx
//<!-- Não havia botão de cancelamento -->
        function editarCliente(id) {
            const cliente = clientes.find(c => c.id === id);
            if (cliente) {
                document.getElementById('nome').value = cliente.nome;
                document.getElementById('email').value = cliente.email;
                document.getElementById('cpf').value = cliente.cpf;
                document.getElementById('telefone').value = cliente.telefone || '';
                document.getElementById('cidade').value = cliente.cidade || '';
                document.getElementById('status').value = cliente.status;
```

**Trecho corrigido**

```html
<button type="button" id="cancelarEdicao" style="display:none" onclick="limparFormulario()">✖️ Cancelar edição</button>

```

**Descrição técnica:**

Adição do botão “Cancelar Edição” e lógica de exibição condicional (`atualizarEstadoEdicao()`).

---

## **9. Situação:** Campo telefone não mostrava exemplo de formato. 📞

**Classificação:** Falha

**Justificativa:** Falta de instrução visual para o usuário sobre o formato esperado.

**Trecho origina:**

```html
<input type="text" id="telefone" name="telefone" placeholder="(00) 00000-0000">

```

**Trecho corrigido :**

```html
<input type="number" id="telefone" name="telefone" placeholder="(00) 00000-0000" pattern="\(\d{2}\) \d{4,5}-\d{4}">
<small>Formato: (00) 00000-0000</small>

```

**Descrição técnica:**

Fornecida indicação de formato esperado via `<small>` e validação adicional com `pattern`. 

---

## **10. Situação:** Sistema não informava data de atualização de cadastro. 🗓️

**Classificação:** Falha

**Justificativa:** Falta de controle de atualização após a edição, impossibilitava verificar o histórico das ultimas atualizações.

**Trecho original:**

```html
<small>Cadastrado em: ${cliente.dataCadastro}</small>

```

**Trecho corrigido (sugestão baseada em melhoria):**

```html
<small>Última atualização: ${cliente.dataAtualizacao || cliente.dataCadastro}</small>

```

**Descrição técnica:**

Implementação sugerida para visualizar as útimas alterações, melhorando localizar as funções de atualizações do cadastro.

---

## **11. Situação:** Campo telefone permitia letras. 🔠

**Classificação:** Erro

**Justificativa:** O tipo `text` aceitava caracteres não numéricos.

**Trecho original** 

```html
<input type="text" id="telefone" name="telefone" placeholder="(00) 00000-0000">

```

**Trecho corrigido**

```html
<input type="number" id="telefone" name="telefone" placeholder="(00) 00000-0000">

```

**Descrição técnica:**

Tipo de input alterado para `number`, garantindo que apenas números sejam aceitos.

---

## **12. Situação:** Campo CPF permitia letras. 🔢

**Classificação:** Erro

**Justificativa:** O campo `text` não restringia entrada numérica.

**Trecho origina**

```html
<input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>

```

**Trecho corrigido**

```html
<input type="number" id="cpf" name="cpf" placeholder="000.000.000-00" required pattern="\d{3}\.\d{3}\.\d{3}-\d{2}">

```

**Descrição técnica:**

Alteração do tipo `text` para `number` com `pattern` numérico assegura consistência nos dados.

---

## **13. Situação:** Sistema permitia cadastro duplicado (mesmo e-mail/CPF). 🚫

**Classificação:** Defeito

**Justificativa:** A função de verificação retornava sempre `false`, permitindo duplicatas, ou seja, se o usuário registrasse outro perfil com os mesmos dados do anterior existente, o sistema permitia.

**Trecho original**

```jsx
function verificarClienteExistente(email, cpf) {
    return false;
}

```

**Trecho corrigido:**   

```jsx
function verificarClienteExistente(email, cpf, ignoredId = null) {
    const emailNorm = (email || '').trim().toLowerCase();
    const cpfNorm = (cpf || '').trim();
    return clientes.some(c =>
        c.id !== ignoredId && (String(c.email).trim().toLowerCase() === emailNorm || String(c.cpf).trim() === cpfNorm)
    );
}

```

**Descrição técnica:**

Lógica reescrita para comparar e-mails e CPFs existentes, evitando duplicações tanto no cadastro quanto na edição.

---

## 📊 **Resumo das Correções**

| Tipo | Quantidade |
| --- | --- |
| **Erros** | 8 |
| **Falhas** | 4 |
| **Defeitos** | 1 |

### **Melhorias importantes:**

- Adição de controle de edição (`editingID`).
- Prevenção de duplicatas por CPF e e-mail.
- Feedback visual completo (mensagens de sucesso e erro).
- Novas validações de formato (CPF, telefone).
- Persistência via `localStorage` foi criado com o intuito de simular um banco de dados.
- Função “Cancelar edição”.

### **O que mudou?:**

Melhoria na **usabilidade**, **integridade dos dados** e **manutenção**.

O sistema passou de um fluxo simples e falho para um CRUD funcional, com validações e persistência local segura.

---

Este relatório tem a função de registrar os erros, falhas e defeitos encontrados no sistema, para ajustar e implementar melhorias em termos de manutenção e fazer testes e aplicações antes de ser utilizado. 

---

Agradeço pela leitura e compreensão!!

Por: Sarah Dyovanna 

Turma: 211

Unidade Curricular - UC10: Realizar testes nas aplicações desenvolvidas
