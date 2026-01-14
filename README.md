# Gerador de QR Code

Pequeno script em Python para gerar QR Codes a partir de uma URL informada no terminal. O arquivo PNG recebe um nome derivado da propria URL (sanitizado) para facilitar a organizacao.

Requisitos
- Python 3.8+ instalado
- Biblioteca `qrcode` instalada:

bash
pip install qrcode[pil]

Como usar
1. Abra o terminal na pasta do projeto:
   ```bash
   cd "c:\Users\nonon\Desktop\Gerador de QR Code\qrcode"
   
2. Rode o script e informe a URL quando solicitado:
   bash
   python gen.py
3. Cole ou digite a URL completa e pressione Enter.
4. O QR Code sera salvo em PNG na mesma pasta. O nome do arquivo e gerado a partir da URL; por exemplo:
   - URL `https://exemplo.com/loja/produto` gera `exemplo.com_loja_produto.png`.

Como funciona (resumo)
- `gen.py` le a URL via `input()`.
- Gera a imagem com `qrcode.make(url)`.
- Cria um nome de arquivo seguro a partir do dominio e caminho da URL (removendo caracteres invalidos e limitando o tamanho).
- Salva o PNG e informa o nome gerado no terminal.

Observacoes
- Evite manter arquivos com o nome `qrcode.py` na mesma pasta, pois isso conflita com a biblioteca `qrcode`.
- Para trocar a URL, basta rodar o script novamente e digitar outra URL.
