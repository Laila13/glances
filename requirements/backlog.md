# Engenharia de Requisitos - MVP: Predictive Disk Space

## 1. Definição do MVP
O MVP consiste em estender o módulo de monitoramento de discos do Glances para calcular a taxa de variação de consumo e exibir no painel uma estimativa textual de "Tempo Restante até 100%" (ex: `TTF: 4.5h` - Time to Full).

## 2. Histórias de Usuário e Critérios de Aceite

### [US01] Visualizar estimativa de esgotamento de disco no terminal (PRIORIZADA PARA IMPLEMENTAÇÃO)
* **História:** Como Administrador de Infraestrutura, quero visualizar o tempo estimado restante para o esgotamento do disco diretamente no painel CLI do Glances, para que eu possa tomar ações preventivas de limpeza antes do colapso do sistema.
* **Critérios de Aceite:**
  * **Dado que** o plugin de disco está ativo e coletando métricas consecutivas,
  * **Quando** o consumo de espaço estiver aumentando de forma linear,
  * **Então** o sistema deve exibir ao lado da barra de uso a métrica `TTF: X.Xh`.
  * **Dado que** o consumo está estável ou diminuindo,
  * **Quando** o cálculo preditivo for executado,
  * **Então** a métrica deve exibir `TTF: N/A` ou ficar oculta.

### [US02] Alerta visual baseado no tempo restante (TTF)
* **História:** Como SysAdmin, quero que o Glances altere a cor da métrica TTF para vermelho quando o tempo restante for menor que 2 horas, para chamar minha atenção imediata.
* **Critérios de Aceite:**
  * **Dado que** o TTF calculado é menor que 2.0 horas,
  * **Quando** a tela do terminal for atualizada,
  * **Então** o texto do TTF deve ser renderizado na cor vermelha (Critical).

### [US03] Configuração da janela de tempo para cálculo preditivo
* **História:** Como Engenheira DevOps, quero poder configurar no arquivo `glances.conf` o intervalo de tempo usado para calcular a tendência, para ajustar a sensibilidade a picos temporários.
* **Critérios de Aceite:**
  * **Dado que** alterei o parâmetro `predictive_window = 600` no arquivo de configuração,
  * **Quando** o Glances iniciar,
  * **Então** os cálculos de tendência devem utilizar o histórico dos últimos 10 minutos (600 segundos).

### [US04] Exportação da métrica preditiva via API JSON
* **História:** Como Desenvolvedor de ferramentas de automação, quero que o campo `time_to_full_hours` esteja disponível no payload do servidor REST do Glances, para que eu possa conservar o dado em scripts externos.
* **Critérios de Aceite:**
  * **Dado que** uma requisição GET é feita para `/api/3/disks`,
  * **Quando** o JSON retornar,
  * **Então** cada objeto de ponto de montagem deve conter a chave `"time_to_full_hours": float`.

### [US05] Habilitar/Desabilitar predição via atalho do teclado
* **História:** Como usuário do terminal, quero apertar a tecla `P` para ocultar ou exibir a coluna de predição, liberando espaço visual quando necessário.
* **Critérios de Aceite:**
  * **Dado que** o painel está exibindo as predições,
  * **Quando** o usuário pressiona a tecla `P`,
  * **Então** a coluna TTF deve desaparecer instantaneamente da interface visual.

## 3. Justificativa de Priorização do MVP
A **[US01]** foi selecionada para implementação no Pull Request porque ela ataca diretamente a dor principal identificada no JTBD (visibilidade preditiva) e valida a lógica matemática de regressão linear básica no backend em Python, servindo de base para todas as outras histórias subsequentes.
