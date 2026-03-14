# Calculadora Científica Python

Esta é uma calculadora científica desenvolvida em Python utilizando a biblioteca `tkinter` para a interface gráfica.

## Funcionalidades

A calculadora suporta as seguintes operações e funções:

- **Operações Aritméticas Básicas**: Adição (`+`), Subtração (`-`), Multiplicação (`*`), Divisão (`/`).
- **Potência**: `^`
- **Funções Científicas**:
    - Seno (`sin`)
    - Cosseno (`cos`)
    - Tangente (`tan`)
    - Logaritmo na base 10 (`log`)
    - Raiz Quadrada (`√`)
- **Constante**: Pi (`π`)
- **Limpar Visor**: `C`
- **Calcular**: `=`

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema.

### Instalação e Execução

1. **Clone o repositório** (se estiver no GitHub, caso contrário, baixe o arquivo `calcCientifica.py`):

   ```bash
   git clone https://github.com/SpetsnazBR/calcCientifica.git
   cd NOME_DO_SEU_REPOSITÓRIO
   ```

2. **Crie e ative um ambiente virtual** (recomendado):

   ```bash
   python -m venv .venv
   ```
   - No Windows:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - No macOS/Linux:
     ```bash
     source ./.venv/bin/activate
     ```

3. **Instale as dependências** (se houver, neste caso, o `tkinter` geralmente vem com o Python, mas o `pip` é bom ter):

   ```bash
   pip install pip
   ```

4. **Execute a calculadora**:

   ```bash
   python calcCientifica.py
   ```

## Estrutura do Código

O projeto consiste em um único arquivo:

- `calcCientifica.py`: Contém a implementação da interface gráfica e a lógica da calculadora científica.
