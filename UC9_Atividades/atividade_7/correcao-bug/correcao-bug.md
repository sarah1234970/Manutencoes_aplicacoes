# Atividade 7 – Versionamento com Git
## Códigos com Erro para a Atividade Versionamento **com Git**

## **1.Python Desktop Simples**

**Desafio 1**

```python
def dividir(a, b):
return a / b
a = 10
b = 0
resultado = dividir(a, b)
print(f"O resultado da divisão é: {resultado}")
```

- Nota-se um erro na linha 5 `dividir(a, b)`  com o “a” valendo 10 e “b” valendo 0, dividindo os dois N resulta em zero, no python a divisão por zero é indefinida, gerando um “ZeroDivisionError”.

Correção:

```python
def dividir(a, b):
    if b == 0: # para informar que o zero nao pode
        return "Erro: Divisão por zero não é permitida."
    else:
         return a / b
a = 10
b = 5 
resultado = dividir(a , b)
print(f"O resultado da divisão é: {resultado}")
```

- Adicionei uma condição para informar que a divisão por zero não é permitida
- Mudei o divisor 0 para outro valor.

---

**Desafio 2**

```python
nome_usuario = "Professor(a)"
print("Olá, " + nome_usuar)
```

- Erro de sintaxe na linha 2 `print("Olá, " + nome_usuar)` o “nome_usuar” não corresponde com a variável “nome_usuario”

Correção:

```python
nome_usuario = "Professor(a)"
print("Olá, " + nome_usuario)
```

- Apenas modifiquei “nome_usuar” para “nome_usuario”

---

**Desafio 3**

```python

frutas = [maçã, "banana", "laranja"]
print(f"Minhas frutas favoritas: {frutas}")
```

- Nota-se que a palavra maçã não tem aspas duplas, ou seja, não vai retornar o resultado esperado

Correção:

```python

frutas = ["maçã", "banana", "laranja"]
print(f"Minhas frutas favoritas: {frutas}")
```

- Adicionei aspas duplas na palavra maçã
- Retorna normalmente as frutas

---

## **2. Web (HTML, CSS e JavaScript)**

**Desafio 4**

```jsx
<!DOCTYPE html>
<html>
<head>
 <title>Bug de Tag</title>
 <link rel="stylesheet" href="style.css">
</head>
<body>
 <h1 class="titulo">Página com Bug de Estrutura</h1>
 
 <p>Este é o primeiro parágrafo. </pa>
 <div id="status">Verificando JS...</div>
 <script src="script.js"></script>
</body>
</html

```

- Nota-se um erro de sintaxe nas tag html “</html” que a tag não foi fechada e  “</pa>” essa tag não existe, seria “</p>”

Correção:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Bug de Tag</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 class="titulo">Página com Bug de Estrutura</h1>

    <p>Este é o primeiro parágrafo. </p>
    <div id="status">Verificando JS...</div>
    <script src="script.js"></script>
</body>
</html>
```

- Fiz o fechamento correto da tag html e fechei o parágrafo com a tag correta.

---

**Desafio 5**

```jsx
.titulo {
 font-size: 24px;
 color: blue
 background-color: yellow;
 padding: 10px;
 border: 1px solid black;
}
```

- Falta um ; depois da definição “color”

Correção:

```css
.titulo {
 font-size: 24px;
 color: blue;
 background-color: yellow;
 padding: 10px;
 border: 1px solid black;
}
```

- Adicionei ; na definição color

---

**Desafio 6**

```jsx
let valor = 5;
let elemento = document.getElementById("status");
if (valor = 10) {
 elemento.innerText = "A condição é sempre verdadeira! (Bug de Lógica)";
} else {
 elemento.innerText = "A condição é falsa.";
}
```

- O valor `let valor = 5;`  está errado pois a condição informa que o valor tem que ser igual a dez
- na linha da condição `if (valor = 10)` falta um = em valor para retornar dez

Correção:

```jsx
let valor = 10;
let elemento = document.getElementById("status");
if (valor == 10) {
    elemento.innerText = "A condição é sempre verdadeira! (Bug de Lógica)";
} else {
    elemento.innerText = "A condição é falsa.";
}
```

- Troque o valor de 5 pelo 10 para retornar corretamente;
- Adicionei mais um “=” na condição

---

## 3. Django(Python Web Framework)

**Desafio 7**

```python
# views.py no app Django
# Tarefa: Descomentar a linha de importação para que HttpResponse funcion
e.
# from django.http import HttpResponse
def saudacao(request):
 return HttpResponse("Olá do Django!")
```

- A tag de importação está comentada
- O código está mal identado

Correção

```python
from django.http import HttpResponse 
    def saudacao(request):
        return HttpResponse("Olá do Django!")
```

- Descomentei e fiz a identação

**Desafio 8**

```python
from django.urls import path
from . import views
def outra_view(request):
	pass
urlpatterns = [
 path('ola/', views.saudacao) 
 path('outra/', views.outra_view),
]
```

- Falta vírgula depois do primeiro path

Correção:

```python
from django.urls import path
from . import views
def outra_view(request):
	pass
urlpatterns = [
 path('ola/', views.saudacao), 
 path('outra/', views.outra_view),
]
```

- adicionei a vírgula de pois do primeiro path em viws.saudacao

## 4. Kivy (Mobile com python)

Desafio 9

```python
# Tarefa: Corrigir o nome da classe 'Ap' para 'App' na linha 1 e 5.
from kivy.app import Ap
from kivy.uix.label import Label
class MinhaApp(Ap):
 def build(self):
 return Label(text='Kivy App com Bug de Importação')
MinhaApp().run()
```

- Nome da classe errada “Ap” na importação
- Classe com o nome errado “Ap”

Correção:

```python
from kivy.app import App
from kivy.uix.label import Label
class MinhaApp(App):
    def build(self):
        return Label(text='Kivy App com Bug de Importação')
MinhaApp().run()
```

- Corrigi o nome tanto da  importação quanto da classe

---

**Desafio 10**

```python
from kivy.app import App
from kivy.uix.button import Button
class OutraApp(App):
 def build(self)
	 Button(text='Corrija o Retorno!').run() 
OutraApp().run()

```

- Falta um “return” depois da função `def build(self)`

Correção:

```python
from kivy.app import App
from kivy.uix.button import Button
class OutraApp(App):
    def build(self):
     return
    Button(text='Corrija o Retorno!').run() 
OutraApp().run()
```

- Adicionei o return e identei algumas linhas
