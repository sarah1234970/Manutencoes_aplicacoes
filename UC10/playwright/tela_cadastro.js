const { chromium } = require('playwright');

(async () => {
  
    const browser = await chromium.launch({
      headless: false,
      channel: 'chrome',
    });
    const page = await browser.newPage();

    console.time('Navegação Chrome Tela');
    await page.goto('http://127.0.0.1:5500/teste/teste2/index.html');
    await page.fill('#username', 'Sarah');
    await page.fill('#email', 'sah@email');
    await page.fill('#cpf', '123.456.789-00');
    await page.click('#telefone', { clickCount: 3 }); // Seleciona o campo telefone
    await page.fill('#telefone', '(11) 98765-4321');
    await page.fill('#cidade', 'Exemplo City');
    await page.click('#submitBtn');
  
console.log('Formulário enviado com sucesso!');
    await page.waitForTimeout(5000);
    console.timeEnd('Navegação Chrome Tela');
    await browser.close();
    })();
