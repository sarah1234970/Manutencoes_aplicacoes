# UC 09 - Atividade de Programação Web 💻- Mini CRUD com JSON e localS

### 🔍 💡**Pesquisa Inicial**

- O que é **JSON**?

O **JSON** (*JavaScript Object Notation*) é, como o nome sugere, uma forma de notação de objetos [**JavaScript**](https://www.alura.com.br/artigos/javascript), de modo que eles possam ser representados de uma forma comum a diversas linguagens. O JSON é conhecido como o **formato padrão para troca de informações entre sistemas web, especialmente em APIs**.

---

- **Para que ele é utilizado no desenvolvimento de sistemas?**

A linguagem JSON é geralmente usada, pela sua simplicidade, legibilidade e suporte amplo. 

- **Simplicidade:** o formato JSON é relativamente simples e fácil de entender. Ele usa uma sintaxe leve e minimalista.
- **Legibilidade:** o JSON é projetado para ser legível tanto por humanos quanto por máquinas. Sua estrutura é organizada e fácil de analisar, facilitando a depuração de erros e o trabalho das pessoas desenvolvedoras;
- **Portabilidade:** ele é independente de plataforma e pode ser utilizado em diferentes linguagens de programação.
- **Suporte amplo:** a maior parte das linguagens de programação possui suporte nativo ou bibliotecas que facilitam a manipulação de dados em formato JSON.
- **Integração com a web:** o JSON é muito utilizado na comunicação entre servidores e clientes em aplicações web, inclusive em APIs (Interface de Programação de Aplicativos), para transferir dados entre servidor e clientes de forma mais simples.

---

- **Qual a diferença entre JSON e um array/objeto do JavaScript?**
    - **A diferença principal é que JSON:**
    - é um formato de texto padronizado para troca de dados
    - aspas duplas são obrigatórias
    - string em formatação de texto
    - usa intercambio de dados
    
    ---
    
    - **Objetos e arrays em JavaScript:**
    - são estruturas de dados nativas da linguagem, usadas para construir aplicativos e possuem uma maior flexibilidade.
    - tem uma manipulação de dados em tempo de execução
    - aspas pode ser duplas ou simples

---

- **Cite um exemplo simples de dado em formato JSON.**

```json
{
   "cliente": {
       "id": 06,
       "nome": "Saruska"
   },
   "pagamentos": [
       {
           "id": 123,
           "descricacao": "Compra do livro Pequeno Principe",
           "valor": 50.5
       },
       {
           "id": 404,
           "descricacao": "Mensalidade escolar",
           "valor": 1500
       }
   ]
}
```

- Não pode ter funções;
- Não pode ter comentários;
- Todo texto sempre tem aspas duplas;
- As propriedades sempre tem aspas duplas.

---

### **Proposta de atividade Atividade📑**

- Desenvolver **lógica de cadastro, listagem e exclusão de itens**.
- Reforçar a manipulação do **DOM** e do **localStorage**.
- Entender como o **JSON** auxilia na **persistência de dados** no navegador.

---
