# 🏆 Sistema de Gestão de Campeonato Esportivo - CLI

## 👤 Alunos

- **Nome:** ALEXSANDHER ANGEL DA CUNHA FERREIRA DA SILVA  
  **RA:** 1986097

- **Nome:** LUIZ FELIPE ROSA DOS SANTOS  
  **RA:** 1996870

- **Nome:** NATAN NUNES DEL BONI  
  **RA:** 1999528

---

## 📚 Descrição Geral

Este projeto consiste em um sistema de linha de comando (CLI - Command Line Interface) escrito em Python, com a temática de **campeonato esportivo**.

O sistema foi desenvolvido como trabalho prático para a disciplina de **Estrutura de Dados**, com o objetivo de aplicar os conceitos fundamentais estudados em aula como **listas**, **filas**, **pilhas**, **tuplas** e **dicionários**.

### Funcionalidades principais:

- ✅ Cadastro de jogadores;
- ✅ Montagem de times;
- ✅ Agendamento de confrontos entre times;
- ✅ Visualização de jogadores cadastrados;
- ✅ Visualização de confrontos agendados.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca `collections` → uso da `deque` para fila
- Tipos de dados nativos: `list`, `dict`, `tuple`

---

## 🧠 Estruturas de Dados Utilizadas

### 🟢 Dicionário (`dict`)
Usado para armazenar:
- Informações dos **jogadores** (`jogadores`)
- Composição dos **times** (`times`)

```python
jogadores[nome] = (idade, posicao)
times[nome_time] = [jogador1, jogador2, ...]
```

### 🟠 Tupla (`tuple`)
Utilizada para representar confrontos:
```python
confrontos.append((time1, time2))
```
Cada confronto é uma tupla com os nomes de dois times.

### 🔵 Lista (`list`)
Usada para armazenar os jogadores em um time:
```python
times[nome_time] = [jogador1, jogador2, ...]
```

### 🔴 Fila (`deque`)
Fila utilizada para organizar a ordem dos confrontos (FIFO):
```python
from collections import deque
confrontos = deque()
```

---

## 🧪 Testes Automatizados

- Foram criados arquivos `.txt` com entradas simuladas para testar os fluxos principais do sistema, como cadastro, montagem de time e confrontos.
- A execução pode ser feita redirecionando o conteúdo do arquivo:
```bash
python main.py < testes/teste1.txt
```

---

## ▶️ Execução

1. Certifique-se de ter o Python 3 instalado.
2. Execute o programa:
```bash
python main.py
```

3. Siga o menu interativo para utilizar o sistema.

---

## 📁 Estrutura do Projeto

```
├── main.py               # Arquivo principal com a lógica do sistema
├── testes/
│   ├── teste1.txt        # Simulação de entrada de dados
│   └── ...
└── README.md             # Este arquivo
```

---

## ✅ Regras e Validações Implementadas

- ❌ Não permite nomes ou posições vazias.
- ❌ Não permite idade inválida (apenas números).
- ❌ Não permite confronto entre times iguais.
- ❌ Não permite cadastrar jogador com nome repetido.
- ❌ Não monta time com jogadores inexistentes.

---

## 📌 Observações

- O código foi dividido em funções simples para facilitar a manutenção e o entendimento.
- A interação é totalmente por terminal, sem interface gráfica.
- O foco do projeto é demonstrar domínio de **estruturas de dados** na prática.

---
