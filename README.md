# 📜 Ravenizer - Windows Update Automator

<img src="https://eduardodossantosferreira.github.io/ravenizer/ravenizer.png" alt="Ravenizer Logo" width="200px" style="background: #fff; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">

**Ravenizer** é uma ferramenta de atualização automatizada para Windows que utiliza `winget` e `Chocolatey` para manter seu sistema e aplicativos sempre atualizados com um único clique.

## ✨ Funcionalidades

- ✅ Atualização completa do sistema via `winget upgrade --all`
- ✅ Atualização de programas via `choco upgrade all -y`
- ✅ Interface intuitiva e amigável
- ✅ Log detalhado de todas as operações
- ✅ Barra de progresso para acompanhamento
- ✅ Design dark mode moderno

## ⚙️ Pré-requisitos

- Windows 10/11
- [App Installer (winget)](https://www.microsoft.com/store/productId/9NBLGGH4NNS1)
- [Chocolatey](https://chocolatey.org/install) (opcional mas recomendado)

## 🚀 Como Usar

1. Execute o Ravenizer
2. Clique em **"INICIAR ATUALIZAÇÃO COMPLETA"**
3. Aguarde enquanto o sistema é atualizado
4. Veja o progresso na barra e detalhes no log

## 📦 Instalação

### Método 1: Executável

Baixe a versão mais recente do [Releases](https://github.com/seu-usuario/ravenizer/releases) e execute o instalador.

### Método 2: Via Python

```bash
git clone https://github.com/seu-usuario/ravenizer.git
cd ravenizer
pip install -r requirements.txt
python main.py
```

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- PySide6 (Qt for Python)
- winget (Gerenciador de Pacotes do Windows)
- Chocolatey (Gerenciador de Pacotes para Windows)

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

Para dúvidas ou sugestões:  
[seu-email@exemplo.com](mailto:seu-email@exemplo.com)  
[Twitter/@seu-usuario](https://twitter.com/seu-usuario)

---

**Nota:** Este projeto não é afiliado à Microsoft ou ao Chocolatey.  
`winget` e `Chocolatey` são ferramentas de terceiros.
