# Atividade 6🚀

Um resumo das alterações feitas e um mini relatório da atividade.

### Botão com função de chamada errada ▶

O botão no  HTML está configurado para chamar uma função chamada `adicionar()`, mas a função escrita em  JS se chama `adicionarTarefa()` entao isso altera a comunicação e faz com que ele não reconheça a função “adicionar”.

- **html:** `<button onclick="adicionar()">Adicionar</button>`
- **no JS:** `function adicionar**Tarefa**() { ... }`

Então como resolver? O nome da função na tag `<button>` precisa ser exatamente o mesmo que o nome da função no script para que o botão realize a função

---

### Operador de Comparação Errado na Condição `if`⚙🎲

Dentro da função, o sistema está tentando verificar se o campo de texto está vazio. No entanto, o código usa o operador de atribuição (`=`) em vez de um operador de comparação que seria (`==` ou `===`).

- **Erro:** `if (valor = "")`
- **O que acontece:** Isso **atribui** um valor vazio à variável `valor` em vez de **comparar** se ela está vazia. Como a atribuição resulta em uma nota “falsa" em JavaScript, o alerta `alert("Digite uma tarefa!");` não aparece. Ou seja, quando for adicionada uma nota sem valor ou conteúdo ela vai ser adicionada na lista.
- **Correção:** Para corrigir podemos adicionar `==` ou `===` para comparar. Ex: `if (valor === "")`

---

### Criação de Elemento de Lista (`li`) com Tag Inválida 📌❎

O código tenta criar um novo item de lista usando `document.createElement("il")`. A tag para adicionar lista (`list item`) em HTML é `li`.

- **Código com erro:** `let li = document.createElement("il");`
- **Correção:** `let li = document.createElement("li");` Corrigindo essa sintaxe,  ele faz uma listagem mais organizada e limpa de visualizar.

---

### Limpeza do campo de texto com problemas 🔍🗑

Ao final da função, o código tenta limpar o campo de input usando a propriedade `innerText`. Elementos `<input>` não usam `innerText`; o texto que eles exibem é controlado pela propriedade `value`.

- **Código com erro:** `input.innerText = "";` isto é quando ele adiciona uma nota, o que foi digitado continua na barra de adicionar.
- **Correção:** `input.value = "";` assim, após adicionar uma nota ele apaga faz a limpeza no campo de texto.
