// Alternar tema escuro/claro
document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggle');
    
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            
            // Opcional: Salvar preferência no localStorage
            const isDarkMode = document.body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDarkMode);
        });

        // Carregar tema salvo (opcional)
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('dark-mode');
        }
    }
});