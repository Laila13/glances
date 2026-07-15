# CSI412 - Engenharia de Software I (UFOP)
## Trabalho Prático: Open Source Discovery & Design (Glances)

Este repositório contém o mapeamento de requisitos, modelagem arquitetural e prototipagem de uma extensão para a ferramenta open-source de monitoramento de sistemas **Glances** (Semestre 2026/1).

---

## 1. Identificação do Grupo

*   **Desenvolvedora e Revisora(Autor do PR):** Laila Ferraz Souza Lima (Matrícula: 19.2.8213)
---

## 2. Escopo da Extensão (MVP)

O objetivo deste projeto é propor e modelar uma melhoria preventiva para o Glances. O foco do MVP é o desenvolvimento de um algoritmo de **Time to Full (TTF)**: um motor analítico que calcula, com base na taxa de consumo recente, estimativas em horas para o esgotamento completo do espaço em disco. 

A proposta visa transformar o monitoramento puramente reativo atual do software em uma ferramenta preventiva para administradores de infraestrutura. A lógica implementada encontra-se isolada no arquivo `predictive_engine.py` na raiz do projeto.

---

## 3. Estrutura do Repositório

O projeto está organizado nos seguintes diretórios, divididos de acordo com as fases de engenharia do trabalho:

| Diretório | Arquivo | Descrição |
| :--- | :--- | :--- |
| [`/discovery`](./discovery) | `discovery.md` | Descrição do ecossistema, definição do framework *Jobs to Be Done* (JTBD), Personas e Mapa de Empatia. |
| [`/requirements`](./requirements) | `backlog.md`<br>`testes.md` | Escopo do MVP, Backlog priorizado com 5 histórias de usuário (Gherkin) e cenários de teste associados. |
| [`/diagrams`](./diagrams) | `diagrams.md` | Arquivos de modelagem UML textual desenvolvidos em Mermaid (Classes, Sequência e Componentes). |
| [`/ai-usage`](./ai-usage) | `ai_usage.md` | Documentação de transparência de uso de IA, registrando os prompts utilizados e as decisões de engenharia tomadas pela dupla. |

---

## 4. Visualização dos Diagramas

Os diagramas de arquitetura foram criados utilizando a especificação **Mermaid** e possuem renderização nativa diretamente na interface web do GitHub. Caso utilize um leitor de markdown local que não suporte a renderização automatizada, a sintaxe textual pode ser copiada e colada no [Mermaid Live Editor](https://mermaid.live).
