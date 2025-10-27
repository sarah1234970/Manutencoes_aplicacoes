### **Pesquisa de Teste de Integração e Dependências (Auto-Estudo)**

## 1. Etapa: Teste de integração de pesquisa 🔍

### Definição e sua Importância:

Os testes de integração são responsáveis por testar a integração entre diferentes partes de um sistema. Tem o objetivo de gerenciar um funcionamento de um elemento num conjunto

Por exemplo, os testes de integração geralmente envolvem a execução de vários testes unitários de forma agrupada, simulando o comportamento do sistema como um todo. Eles são executados em diferentes níveis do sistema, testando a interação entre diferentes módulos e serviços. Um exemplo prático de teste de integração seria verificar se o cadastro de um usuário no sistema está funcionando corretamente quando integrado com o envio de e-mails de confirmação. Para isso, seria necessário criar um teste que simule a ação de cadastrar um usuário e verificar se o e-mail de confirmação foi enviado corretamente.

### Tipos de teste de integração:

- Teste de integração Big Bang
    
    Outra forma de realizar testes de integração é por meio da integração tipo big bang. Nesse caso, todas as unidades, componentes e módulos do sistema são integrados e testados de uma só vez, como se formassem uma única unidade. O teste big bang oferece uma resposta rápida quando o sistema funciona corretamente com todos os seus elementos.
    
    No entanto, essa forma de teste é limitada. Se o processo mostrar que o sistema não funciona como deveria, o teste big bang não indica quais partes estão falhando na integração.
    
- Teste Incremental

O teste incremental funciona como uma abordagem do teste de integração. Esse tipo de teste faz a utilização de “stubs” e “drivers” que é um método de teste incremental que integra os módulos um por um.

<aside>
💡

**Stubs** são implementações simplificadas de **módulos de nível inferior** usados em testes de integração de cima para baixo, enquanto **drivers** simulam **módulos de nível superior** em testes de integração de baixo para cima.

Vários stubs e drivers são usados para testar os módulos consecutivamente e descobrir bugs. O teste incremental envolve testar um módulo, conectá-lo a outro módulo e verificar sua integração. Em seguida, adiciona-se outro módulo para continuar com as mesmas etapas.

</aside>

- Teste Top Down

O teste de integração de software de Top Donwn (cima para baixo) é uma das categorias de testes de integração em que as unidades de alto nível são testadas primeiro, seguidas pelas unidades de nível inferior. Após esse processo, a integração é considerada concluída para garantir que o software esteja funcionando conforme o esperado. Os drivers e stubs são desenvolvidos para realizar o teste de integração de software de top down.

**Como esse tipo de teste é usado**

**Etapa 1** − Nessa abordagem, o driver denota o módulo de controle proeminente chamado componente de alto nível e o stub denota o componente de nível inferior que funciona diretamente sob esses módulos de nível superior.

**Etapa 2** - O teste começa de cima para baixo, portanto, os componentes de nível mais alto são verificados primeiro de forma independente.

**Etapa 3** − Em seguida, os componentes de nível inferior, também conhecidos como stubs, substituem os componentes de nível superior sequencialmente, um por um.

**Etapa 4** − Este processo continua até que cada um dos componentes seja combinado e verificado.

**Etapa 5** – Um stub diferente substitui o módulo de controle atual após a execução de cada conjunto de casos de teste. Esses stubs são considerados a substituição de curto prazo de um módulo e produzem o mesmo resultado que o software.

**Etapa 6** − Para verificar a presença de quaisquer bugs, casos de teste de regressão são executados para verificar se há algum efeito colateral.

---

## **2- Etapa : explorar dependências em aplicativos de software☑️**

- **Dependências:**
    
    Uma dependencia de software é uma conexão em que um software depende de outro para funcionar. É como um componente adicionado no seu aplicativo para “ativar” alguma funcionalidade. 
    
- **Exemplos de dependências**:
As dependências podem incluir:
    - Bibliotecas: codigos pré-escritos que fornecem uma função específica
    - Frameworks: modelo de construção de aplicativos
    - Módulos: são unidades de código independentes que oferecem outros recursos
    - APIs: Interfaces que permitem que diversos componentes tenham uma comunicação entre eles.
- **Exemplos de Dependências em um Aplicativo Remoto**
1. **Dependência de um sistema de banco de dados** 

| **Detalhe** | **Descrição** |
| --- | --- |
| **O que é:** | O aplicativo (um e-commerce) depende de um serviço de banco de dados (Sql, MongoDB ou PostgreSql) para guardar os dados e recuperar dados do cliente, produtos e outros fins de histórico. |
| **Natureza:** | **Dependência de Serviço Externo.** O aplicativo envia consultas remotamente ao servidor de banco de dados. |

**Como afeta o Desempenho e a Funcionalidade**

- **Atraso no Desempenho:** Se a conexão de rede entre o aplicativo e o banco de dados for lenta, ou se o banco de dados estiver sobrecarregado, as consultas demorarão a retornar. Isso aumenta o **tempo de resposta** do aplicativo.
- **Falha na Funcionalidade:** Se o servidor de banco de dados cair (ficar *offline*), a dependência é **quebrada**. O aplicativo não conseguirá ler ou gravar dados e falhará em qualquer funcionalidade que exija acesso a dados (ex: login de usuário, exibição do catálogo de produtos).

---

**2. Dependência de uma API de Autenticação/Login (Terceiro)**

| **Detalhe** | **Descrição** |
| --- | --- |
| **O que é:** | O aplicativo usa um serviço de terceiros (ex: Google Sign-In, ou um serviço de microserviço interno) para gerenciar o login e a identidade dos usuários. |
| **Natureza:** | **Dependência de API Externa.** O aplicativo faz chamadas de rede para a API de autenticação. |

**Como afeta o Desempenho e a Funcionalidade**

- **Tempo de resposta:** cada tentativa de login para verificar o token, pede uma chamada de rede para API. Se ela tiver um tempo de inatividade ou um tempo de resposta alto, o processo de login ou o acesso a recursos protegidos será **lento** para o usuário.
- **Bloqueio na funcionalidade:** 
Se a API de autenticação falhar ou o aplicativo não conseguir se encontrar com ela, o aplicativo **perderá sua funcionalidade de segurança**. Os usuários não conseguirão fazer login ou registrar-se, tornando o aplicativo inutilizável para a maioria das tarefas.
- **Gerenciando dependências**:

Na criação de aplicativos de software, os desenvolvedores utilizam uma variedade de linguagens de programação e ferramentas. Entretanto, esses aplicativos e sistemas não existem isoladamente; eles dependem fortemente de outros componentes de software conhecidos como dependências

**Ferramentas e estratégias para gerenciar dependências de software**

- **Realizar análise de composição de software: A** Análise de Composição de Software (SCA) é um processo e conjunto de ferramentas que examina a cadeia de fornecimento de software e analisa a composição de um aplicativo de software.
Ele se concentra na identificação e no gerenciamento de componentes de código aberto e bibliotecas de terceiros usados em um projeto de software.
As ferramentas SCA detectam e relatam vulnerabilidades conhecidas, problemas de licenciamento e riscos de conformidade associados às dependências do software.-

- **Gerenciador de pacotes** : Um gerenciador de pacotes é uma ferramenta de software que ajuda a gerenciar a instalação, atualização e remoção de pacotes de software ou bibliotecas.
Ele simplifica o processo de gerenciamento de dependências ao manipular automaticamente a recuperação e a instalação dos componentes necessários dos repositórios.
Os gerenciadores de pacotes garantem que as **dependências necessárias** estejam disponíveis e devidamente integradas a um projeto de software.

---

### 3 - Etapa : Ferramentas e técnicas para teste🛠️

1. **Ferramentas de teste**: Pesquise várias ferramentas usadas para testes de integração e dependências. Crie uma tabela que inclua:
    - O nome da ferramenta
    - Uma breve descrição de suas características
    - As vantagens de usar esta ferramenta
    
    | **Ferramenta** | **Descrição / Características** | **Vantagens** | **Desvantagens** |
    | --- | --- | --- | --- |
    | **Transferidor (Protractor)** | Uma ferramenta de testes desenvolvida para aplicações web com **Angular** e **AngularJS**. Simula interações do usuário (cliques, preenchimento de formulários). | 1. Aguarda automaticamente que o aplicativo esteja pronto antes de executar os testes, reduzindo erros de carregamento lento. 2. Pode ser usado com bibliotecas de teste como **Jasmine** e **Mocha**, oferecendo flexibilidade. | 1. Tem dificuldades para ter bom desempenho com **aplicativos que não são Angular**, limitando a usabilidade. 2. O recurso de espera automática pode tornar os testes **mais lentos**. |
    | **Jasmine** | Um framework de testes **JavaScript** popular para escrever **testes unitários** para aplicações web. É orientado por comportamento (Behavior-Driven Development - BDD), focando em como a aplicação deve se comportar. | 1. A **sintaxe simples** torna fácil para desenvolvedores iniciantes e experientes escreverem testes rapidamente. 2. Não requer nenhuma biblioteca ou ferramenta adicional para ser executado, o que o torna **leve e fácil de configurar**. | 1. Tem **suporte limitado para testes assíncronos**, exigindo configuração adicional e complexidade de código. 2. Os **recursos de relatórios prontos para uso são limitados**, necessitando de integrações de terceiros para relatórios detalhados. |
    | **HiperTeste** | Um framework de teste de nível avançado para aplicações web atuais. Foca em **testes de ponta a ponta**, garantindo que as aplicações funcionem conforme o esperado pelo ponto de vista do usuário. | 1. Simula **interações reais do usuário**, garantindo que o aplicativo funcione corretamente. 2. A estrutura é **simples de instalar e configurar**, permitindo que os desenvolvedores comecem a testar rapidamente. | 1. Os **custos de licenciamento** podem ser restritos para equipes menores ou startups com orçamentos limitados. 2. Podem ocorrer **tempos de execução de testes mais lentos**, especialmente com conjuntos de testes maiores ou aplicativos mais complexos. |
    | **Carteiro**  | Uma plataforma de colaboração para **desenvolvimento de APIs**, garantindo que equipes projetem, testem e documentem APIs com mais eficácia. Sua interface simplifica os testes, oferecendo suporte a testes automatizados. | 1. Fácil de navegação, tornando os **testes de API acessíveis** para todos os níveis de habilidade. 2. As equipes podem **compartilhar coleções, ambientes e documentação** facilmente. | 1. Grandes coleções com muitas solicitações podem tornar a **execução mais lenta**. 2. A **versão gratuita oferece recursos de colaboração limitados**, o que pode prejudicar a eficiência em projetos compartilhados. |

**Citações** 

### Algumas fontes que utilizei para realizar a pesquisa:

> **Alura.** (2021). *Tipos de testes: quais os principais e por que utilizá-los?* https://cursos.alura.com.br/forum/topico-duvida-como-funcionam-os-testes-de-integracao-282533
> 

> **BrowserStack.** (2024). *As 15 principais ferramentas de teste de integração*. https://www.browserstack.com/guide/top-integration-testing-tools
> 

> **BrowserStack.** (2025). *O que é teste de integração*. https://www.browserstack.com/guide/integration-testing
> 

> **Objective.** (2023). *Testes de integração: conheça os tipos e as vantagens em automatizar*. https://www.objective.com.br/insights/teste-de-integracao/
> 

> **TutorialsPoint.** (2023). *Top down integration testing*. [https://www.tutorialspoint.com/software](https://www.google.com/search?q=https://www.tutorialspoint.com/software)_testing_dictionary/top_down_integration_testing.htm
> 

**Atividade remota -** 

---

Agradeço pela leitura e analise da atividade!

Por: Sarah Dyovanna

Turma: 211

Unidade Curricular - UC10: Realizar testes nas aplicações desenvolvidas
