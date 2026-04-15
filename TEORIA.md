# Parte Teórica — Análise e Discussão

**Trabalho:** Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento
**Disciplina:** Algoritmos e Lógica de Programação
**Instituição:** UniFECAF

---

## 1. Contextualização do Desafio

A indústria moderna enfrenta um desafio constante: garantir a qualidade dos produtos fabricados sem comprometer a velocidade e o custo da produção. Quando esse processo é feito manualmente, erros humanos são inevitáveis — um inspetor cansado pode deixar passar uma peça fora do padrão, ou reprovar uma peça boa por falta de atenção. Cada erro gera retrabalho, desperdício de material e aumento nos custos operacionais.

A automação digital resolve esse problema ao substituir o julgamento subjetivo por critérios objetivos e imutáveis aplicados de forma consistente a cada peça. Um sistema automatizado não se cansa, não erra por distração e processa centenas de peças no mesmo tempo em que um inspetor avaliaria uma dezena.

Nesse contexto, o presente protótipo simula a lógica de um sistema de controle de qualidade industrial: recebe os dados de cada peça produzida, aplica os critérios de aprovação definidos pela engenharia e organiza o armazenamento das peças aprovadas — tudo de forma automática e rastreável.

---

## 2. Estrutura do Raciocínio Lógico

O sistema foi desenvolvido com base em quatro pilares fundamentais da lógica de programação:

### 2.1 Funções (`def`)

Cada responsabilidade do sistema foi encapsulada em uma função dedicada. Isso evita repetição de código e torna cada parte do sistema fácil de entender, testar e modificar de forma independente. Exemplos:

- `avaliar_peca(peso, cor, comprimento)` — aplica os critérios de qualidade e retorna o resultado
- `adicionar_em_caixa(caixas, peca)` — gerencia o armazenamento sem que o restante do sistema precise conhecer os detalhes dessa lógica
- `gerar_relatorio(pecas, caixas)` — consolida e exibe os dados finais

### 2.2 Condições (`if / elif / else`)

A lógica de aprovação é inteiramente baseada em estruturas condicionais. Para cada critério (peso, cor e comprimento), o sistema verifica se o valor da peça está dentro do intervalo permitido. Quando um critério não é atendido, o motivo é registrado:

```python
if not (PESO_MIN <= peso <= PESO_MAX):
    motivos.append(f"peso {peso}g fora do intervalo [95g, 105g]")
```

Uma peça pode acumular múltiplos motivos de reprovação, o que fornece ao operador uma informação precisa sobre o que está errado.

### 2.3 Repetição (`while / for`)

O menu principal opera em um laço `while True`, que continua executando até que o usuário escolha a opção de saída. Isso garante que o sistema permaneça disponível para múltiplas operações em uma única sessão.

Laços `for` são usados para percorrer listas de peças e caixas ao gerar listagens e relatórios, processando cada elemento de forma sequencial.

### 2.4 Estruturas de Dados (listas e dicionários)

Cada peça é representada como um dicionário Python, contendo seus atributos (`id`, `peso`, `cor`, `comprimento`, `status`, `motivo`). As peças são armazenadas em uma lista, o que permite iterar, filtrar e remover elementos com facilidade.

O mesmo padrão é adotado para as caixas: cada caixa é um dicionário com número, lista de peças e estado (aberta ou fechada).

---

## 3. Benefícios da Solução e Desafios Enfrentados

### Benefícios

- **Consistência:** os critérios de qualidade são aplicados da mesma forma para todas as peças, sem variação humana.
- **Rastreabilidade:** cada peça reprovada tem seu motivo registrado, facilitando análises e auditorias.
- **Organização automática:** o sistema controla o armazenamento em caixas sem intervenção manual, fechando a caixa cheia e abrindo uma nova automaticamente.
- **Relatório consolidado:** ao final da operação, o sistema entrega uma visão completa da produção em segundos.

### Desafios Enfrentados

- **Consistência dos dados de entrada:** foi necessário tratar entradas inválidas do usuário (letras onde se espera número, IDs duplicados) para evitar que o programa quebrasse. Isso foi resolvido com laços de validação combinados com `try/except`.
- **Remoção de peças aprovadas:** ao remover uma peça que já havia sido alocada em uma caixa, era necessário localizá-la dentro da estrutura de caixas e removê-la de lá também — mantendo a integridade dos dados em dois lugares ao mesmo tempo.
- **Separação de responsabilidades:** organizar o código em módulos distintos (`pecas.py`, `caixas.py`, `relatorio.py`) exigiu cuidado para evitar dependências circulares e manter cada módulo coeso.

---

## 4. Reflexão Final — Expansão para um Cenário Real

O protótipo desenvolvido valida a lógica central do sistema. Em um ambiente industrial real, essa solução poderia ser expandida em diversas direções:

### Integração com Sensores IoT

Em vez de o operador digitar os dados manualmente, sensores instalados na linha de produção coletariam peso, comprimento e cor de forma automática e em tempo real. Os dados seriam enviados diretamente ao sistema via protocolos como MQTT ou OPC-UA, eliminando a intervenção humana no processo de inspeção.

### Visão Computacional com Inteligência Artificial

A identificação de cor poderia ser feita por câmeras acopladas à linha de montagem, usando modelos de visão computacional (como redes neurais convolucionais) para classificar a cor da peça com precisão. Isso tornaria o sistema imune a variações de iluminação e subjetividade humana.

Além disso, algoritmos de aprendizado de máquina poderiam identificar padrões de defeito que vão além dos critérios fixos — detectando anomalias visuais, irregularidades de superfície ou deformações sutis que um critério numérico simples não capturaria.

### Integração com Sistemas ERP

Os dados gerados pelo sistema (peças aprovadas, reprovadas, caixas) poderiam ser enviados automaticamente a sistemas de gestão industrial como SAP ou TOTVS, alimentando relatórios de produção, controle de estoque e rastreabilidade do produto acabado.

### Persistência de Dados

O protótipo atual armazena os dados em memória durante a execução. Em produção, os dados seriam persistidos em um banco de dados relacional (como PostgreSQL) ou em nuvem, permitindo histórico, auditoria e análise de tendências ao longo do tempo.

---

Em suma, o protótipo demonstra que a lógica central de um sistema de automação industrial pode ser construída com conceitos fundamentais de programação. A passagem desse protótipo para um sistema real de produção não exigiria reescrever a lógica — apenas conectá-la a fontes de dados reais e integrá-la à infraestrutura existente da empresa.
