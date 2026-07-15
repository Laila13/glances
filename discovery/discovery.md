# Fase I: Discovery e Design Thinking

## 1. Descrição do Sistema
O Glances é uma ferramenta open-source de monitoramento de sistemas em tempo real, desenvolvida em Python. Ele adota uma abordagem "tudo em um", exibindo métricas de CPU, memória, processos, rede e disco em uma interface de terminal (CLI), Web UI ou exportando via API (JSON/InfluxDB).

## 2. Jobs to Be Done (JTBD)
* **Situação:** Quando estou gerenciando servidores de produção ou ambientes de infraestrutura crítica...
* **Motivação (Job):** Eu quero antecipar gargalos e falhas de recursos antes que eles derrubem os serviços...
* **Resultado Esperado:** Para que eu possa agir de forma preventiva, garantindo 100% de uptime sem precisar olhar gráficos retroativos o tempo todo.

### Lacuna/Oportunidade Identificada
Atualmente, o Glances mostra o consumo de disco reativo. Se um processo começar a gerar logs massivos repentinamente, o administrador só saberá quando o limite crítico for atingido. A oportunidade está em adicionar uma métrica preditiva linear ("Tempo Restante até o Disco Encher").

## 3. Personas

### Persona 1: Tiago, O Administrador de Infraestrutura (SysAdmin)
* **Perfil:** 34 anos, trabalha em uma empresa de e-commerce tradicional. Gerencia 45 servidores Linux antigos e virtuais.
* **Dores:** Acordar de madrugada com alertas de "Disco Cheio" causados por logs mal rotacionados.
* **Necessidade:** Uma métrica direta no painel que avise: "Nesse ritmo, este disco falhará em 3 horas".

### Persona 2: Mariana, Engenheira DevOps
* **Perfil:** 27 anos, focada em automação, CI/CD e ambientes conteinerizados (Docker/K8s).
* **Dores:** Ferramentas pesadas de monitoramento que consomem muita memória nos nós dos clusters.
* **Necessidade:** Métricas leves expostas via JSON pelo Glances para que ela possa criar scripts automatizados de limpeza de disco.

## 4. Mapa de Empatia (Focado em Tiago)
* **O que pensa e sente?** "Preciso manter a estabilidade dos servidores. Detesto monitoramentos complexos que exigem dashboards gigantescos para ver o óbvio."
* **O que vê?** Alertas vermelhos piscando no terminal quando já é tarde demais.
* **O que fala e faz?** Usa o Glances no terminal via SSH diariamente por ser leve, mas sente falta de inteligência preventiva.
* **O que ouve?** Do chefe: "Por que o sistema caiu de novo por falta de espaço em disco se temos monitoramento?"
* **Dores:** Falta de tempo para analisar tendências de consumo de dados manualmente.
* **Necessidades:** Automação simples e predições baseadas no consumo atual.
