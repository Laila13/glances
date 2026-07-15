# Relatório de Uso Crítico de Inteligência Artificial

## 1. Prompts Utilizados

### Fase de Discovery
> "Atue como um Engenheiro de Software Sênior especialista em arquitetura Linux. Analise o repositório open-source Glances (Python). Identifique cenários baseados no framework Jobs to Be Done (JTBD) onde administradores de sistemas enfrentam problemas de monitoramento de armazenamento reativo e sugira uma melhoria preditiva viável para um MVP."

### Fase de Modelagem e Requisitos
> "Crie 5 histórias de usuário utilizando a estrutura corporativa ágil (Como, Quero, Para que) com seus respectivos critérios de aceite baseados em comportamento (Dado, Quando, Então) para um plugin preditivo de tempo de esgotamento de disco no Glances. Em seguida, escreva diagramas de classe e sequência no formato textual do Mermaid."

## 2. Decisões Justificadas e Reflexão Crítica
A IA sugeriu inicialmente uma abordagem estatística complexa utilizando bibliotecas como `scikit-learn` para fazer a predição do consumo de disco por meio de Machine Learning.

**Decisão Humana Interventiva:** Nós rejeitamos a sugestão de usar Machine Learning complexo porque isso violaria uma premissa fundamental do Glances: **ser leve e ter pouquíssimas dependências pesadas**. Em vez disso, guiamos a IA para arquitetar uma solução puramente matemática baseada em **Regressão Linear Simples** usando apenas variáveis de tempo (`time.time()`) e deltas de bytes fornecidos pela biblioteca nativa `psutil`. Isso manteve o MVP viável, leve e fiel à filosofia do projeto original.
