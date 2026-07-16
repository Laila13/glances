# Diagramas de Modelagem UML Textual

## 1. Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    actor SysAdmin as Usuário/Terminal
    participant Main as GlancesCore
    participant Plugin as DisksPlugin
    participant Calc as PredictiveEngine
    participant OS as Sistema Operacional (psutil)

    SysAdmin->>Main: Inicia o Glances
    loop A cada ciclo de atualização (refresh rate)
        Main->>Plugin: update()
        Plugin->>OS: Coleta uso atual do disco (bytes usados, timestamp)
        OS-->>Plugin: Retorna (usado: 75GB, total: 100GB)
        Plugin->>Calc: calculaTendencia(historicoMetricas)
        alt Consumo Crescente (Tendência Positiva)
            Calc-->>Plugin: Retorna TTF em horas (ex: 4.5h)
            Plugin->>Main: Atualiza tela com "TTF: 4.5h"
        else Consumo Estável ou Decrescente
            Calc-->>Plugin: Retorna None / N/A
            Plugin->>Main: Oculta indicador ou exibe "TTF: N/A"
        end
    end
