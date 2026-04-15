# Gestão de Peças — Controle de Qualidade

Sistema de automação digital desenvolvido em Python para controle de produção e qualidade de peças industriais. O sistema avalia cada peça cadastrada contra critérios de qualidade pré-definidos, armazena as aprovadas em caixas com capacidade limitada e gera relatórios consolidados.

---

## Funcionalidades

- Cadastro de peças com avaliação automática de qualidade
- Armazenamento de peças aprovadas em caixas (máximo 10 peças por caixa)
- Fechamento automático de caixa ao atingir capacidade e abertura de nova
- Listagem de peças aprovadas e reprovadas com motivo da reprovação
- Remoção de peças cadastradas
- Listagem de caixas fechadas
- Relatório final consolidado

---

## Critérios de Qualidade

| Critério     | Regra                      |
|--------------|----------------------------|
| Peso         | Entre 95g e 105g           |
| Cor          | Azul ou Verde              |
| Comprimento  | Entre 10cm e 20cm          |

Uma peça pode ser reprovada por um ou mais critérios simultaneamente.

---

## Pré-requisitos

- Python 3.x instalado
- Sem dependências externas (usa apenas bibliotecas padrão)

Verifique sua versão do Python:

```bash
python3 --version
```

---

## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/visepol/unifecaf-python-project.git
cd unifecaf-python-project
```

2. Execute o programa:

```bash
python3 main.py
```

---

## Estrutura do Projeto

```
unifecaf-python-project/
├── main.py         # Menu interativo e ponto de entrada
├── pecas.py        # Lógica de avaliação, cadastro e listagem de peças
├── caixas.py       # Gerenciamento de caixas de armazenamento
├── relatorio.py    # Geração do relatório final consolidado
└── README.md       # Documentação do projeto
```

---

## Exemplos de Uso

### Cadastrar uma peça aprovada

```
Escolha uma opção: 1

--- Cadastrar Nova Peça ---
ID da peça: 1
Peso (g): 100
Cor: azul
Comprimento (cm): 15

Peça #1 APROVADA e adicionada a uma caixa.
```

### Cadastrar uma peça reprovada

```
Escolha uma opção: 1

--- Cadastrar Nova Peça ---
ID da peça: 2
Peso (g): 80
Cor: vermelho
Comprimento (cm): 5

Peça #2 REPROVADA. Motivo: peso 80g fora do intervalo [95g, 105g]; cor 'vermelho' inválida (permitidas: azul, verde); comprimento 5cm fora do intervalo [10cm, 20cm]
```

### Listar peças

```
Escolha uma opção: 2

--- Lista de Peças ---

APROVADAS (1):
  ID 1 | Peso: 100g | Cor: azul | Comprimento: 15cm

REPROVADAS (1):
  ID 2 | Peso: 80g | Cor: vermelho | Comprimento: 5cm
    Motivo: peso 80g fora do intervalo [95g, 105g]; cor 'vermelho' inválida (permitidas: azul, verde); comprimento 5cm fora do intervalo [10cm, 20cm]
```

### Relatório final (com 12 aprovadas e 2 reprovadas)

```
Escolha uma opção: 5

==========================================
         RELATÓRIO FINAL DO SISTEMA
==========================================

Total de peças cadastradas : 14
Total de peças aprovadas   : 12
Total de peças reprovadas  : 2

Caixas fechadas            : 1
Caixa em aberto            : #2 (2/10 peças)

--- Detalhes das Reprovações ---
  ID 13 | Motivo: ...
  ID 14 | Motivo: ...

--- Detalhes das Caixas Fechadas ---
  Caixa #1: peças 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

==========================================
```

---

## Menu do Sistema

```
==========================================
   GESTÃO DE PEÇAS — CONTROLE DE QUALIDADE
==========================================
  1. Cadastrar nova peça
  2. Listar peças aprovadas/reprovadas
  3. Remover peça cadastrada
  4. Listar caixas fechadas
  5. Gerar relatório final
  0. Sair
------------------------------------------
```
