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
        Note over Calc: Aplica Regressão Linear Simples<br/>ΔUso / ΔTempo
        Calc-->>Plugin: Retorna TimeToFull (ex: 3.5 horas)
        Plugin->>Main: Retorna Dicionário de Métricas + TTF
        Main->>SysAdmin: Renderiza na tela "Disk UI (TTF: 3.5h)"
    end
classDiagram
    class GlancesPlugin {
        +str name
        +dict stats
        +update() void
    }

    class GlancesDisksPlugin {
        -list history_samples
        -int max_samples
        +update() dict
        +get_ttf_string() str
    }

    class PredictiveEngine {
        +calculate_hours_to_full(list samples, float total_capacity) float
    }

    class DiskSample {
        +float timestamp
        +float bytes_used
    }

    GlancesPlugin <|-- GlancesDisksPlugin
    GlancesDisksPlugin --> PredictiveEngine : utiliza
    GlancesDisksPlugin --> DiskSample : armazena histórico
graph TD
    subgraph Glances Architecture
        UI[Glances CLI / Web UI View]
        Core[Glances Core Engine]
        PluginContainer[Plugins Manager]
        
        subgraph Disk Component System
            DiskPlugin[Glances Disks Plugin]
            PredictiveModule[Predictive Engine]
        end
    end

    subgraph OS Kernel Layer
        PSUtil[psutil Library]
        DiskDrivers[File System / sys/fs]
    end

    UI --> |Pede Atualização de Tela| Core
    Core --> |Gerencia Ciclo de Vida| PluginContainer
    PluginContainer --> |Chama Update| DiskPlugin
    DiskPlugin --> |Analisa Amostras Temporais| PredictiveModule
    DiskPlugin --> |Busca Métricas Cruas| PSUtil
    PSUtil --> |Queries C / Syscalls| DiskDrivers
graph TD
    subgraph Glances_Core [Componentes Core do Glances]
        Core[Glances Core Engine]
        Plugins[Gerenciador de Plugins]
        Core --> Plugins
    end

    subgraph Predictive_Extension [Módulo Preditivo - Nosso MVP]
        DiskPlugin[Plugin de Disco]
        PredictiveEngine[Motor Preditivo]
        SampleCollector[Coletor de Amostras de Armazenamento]
        
        DiskPlugin --> PredictiveEngine
        PredictiveEngine --> SampleCollector
    end

    subgraph OS [Nível do Sistema Operacional]
        PSUtil[Biblioteca psutil]
        Storage[Armazenamento de Disco]
        PSUtil -.-> Storage
    end

    Plugins --> DiskPlugin
    DiskPlugin --> PSUtil
