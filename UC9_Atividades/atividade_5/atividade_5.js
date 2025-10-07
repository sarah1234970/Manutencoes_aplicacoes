//criei uma simulacao para validar o formulario 
function enviarFormulario() {
    if (enviarFormulario()) {
        let form = document.getElementById("formCadastro");

        // adiquiri as info do formulario
        let dados = {
            nome: form.nome.value,
            email: form.email.value,
            senha: form.senha.value,
            telefone: form.telefone.value,
            idade: form.idade.value
        };

        // Simulação: apenas exibe no console
        console.log("Enviando dados (simulação):", dados);

        //uma simulacao de envio usando uma API fake
        fetch("https://jsonplaceholder.typicode.com/posts", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        })
        .then(res => res.json())
        .then(data => {
            alert("Formulário enviado com sucesso (simulação)!");
            console.log("Resposta do servidor fake:", data);
        })
        .catch(err => {
            alert("Erro na simulação de envio.");
            console.error(err);
        });
    }
}
