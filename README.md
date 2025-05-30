# 🏆 Sistema de Gestão de Campeonato Esportivo - CLI

## 👤 Alunos

- **Nome:** ALEXSANDHER ANGEL DA CUNHA FERREIRA DA SILVA 
- **RA:** 1986097

- **Nome:** LUIZ FELIPE ROSA DOS SANTOS  
- **RA:** 1996870

- **Nome:** NATAN NUNES DEL BONI  
- **RA:** 1999528

---

## 📚 Descrição Geral

Este projeto consiste em um sistema de linha de comando (CLI - Command Line Interface) escrito em Python, com a temática de **campeonato esportivo**.

O sistema foi desenvolvido como trabalho prático para a disciplina de **Estrutura de Dados**, com o objetivo de aplicar os conceitos fundamentais estudados em aula como **listas**, **filas**, **pilhas**, **tuplas** e **dicionários**.

O programa permite:

- Cadastro de jogadores;
- Montagem de times;
- Agendamento de confrontos entre times;
- Visualização de jogadores cadastrados;
- Visualização de confrontos agendados.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Coleção `deque`** da biblioteca `collections`
- Tipos de dados nativos: `list`, `dict`, `tuple`

---

## 🧠 Estruturas de Dados Utilizadas

### ✅ Dicionário (`dict`)

Utilizado para armazenar:

- Informações dos **jogadores** (`self.jogadores`)
- Composição dos **times** (`self.times`)

Exemplo:
```python
self.jogadores[nome] = {'idade': idade, 'posicao': posicao, 'time': None}
