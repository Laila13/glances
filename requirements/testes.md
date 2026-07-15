# Cenários de Teste - US01 (Visualizar estimativa de esgotamento de disco)

## Cenário 1: Consumo de disco linear crescente (Caminho Feliz)
* **Objetivo:** Validar se o cálculo matemático exibe o tempo correto.
* **Entradas simuladas:**
  * Tempo T0: Uso do disco = 50 GB
  * Tempo T1 (após 1 hora): Uso do disco = 60 GB
  * Capacidade Total: 100 GB
* **Passos:**
  1. Iniciar o módulo de disco com a série temporal simulada de crescimento estável de 10 GB/h
  2. Aguardar a atualização do ciclo de métricas.
* **Resultado Esperado:** O sistema calcula que faltam 40 GB para lotar. Na taxa de 10 GB/h, o terminal deve exibir claramente: `TTF: 4.0h`.

## Cenário 2: Consumo estável sem alterações (Exceção/Fronteira)
* **Objetivo:** Garantir que o sistema não quebre por divisão por zero ou exiba valores infinitos.
* **Entradas simuladas:**
  * Tempo T0: Uso do disco = 50 GB
  * Tempo T1 (após 1 hora): Uso do disco = 50 GB
  * Capacidade Total: 100 GB
* **Passos:**
  1. Simular coletas consecutivas sem nenhuma variação no espaço em disco.
* **Resultado Esperado:** A taxa de variação é 0. O sistema deve tratar a exceção internamente e renderizar `TTF: N/A` de forma limpa, sem estourar erros no console.

## Cenário 3: Liberação de espaço em disco (Caminho Alternativo)
* **Objetivo:** Testar o comportamento quando o usuário apaga arquivos.
* **Entradas simuladas:**
  * Tempo T0: Uso do disco = 80 GB
  * Tempo T1 (após 5 minutos): Uso do disco = 40 GB (limpeza de logs)
* **Passos:**
  1. Simular uma queda brusca no uso de armazenamento no intervalo entre coletas.
* **Resultado Esperado:** Como a tendência é negativa (o espaço está aumentando, não acabando), o painel não deve exibir um tempo de falha positivo. O display deve ocultar o indicador ou exibir `TTF: N/A`.
