# Project Evolver Framework

## Português (Brasil)

**Descrição:** O Project Evolver Framework é um conjunto modular orientado por IA, criado para mapear, investigar e corrigir automaticamente problemas estruturais em projetos de software. Ele funciona como um *framework* de três etapas – **Mapeador**, **Explorador de Campo** e **Injetor de Evolução** – que correspondem às fases de diagnóstico e refino do projeto. Na primeira etapa, o *Project-Evolver-Mapper* realiza uma análise geral (“Entrevista de Visão Proativa”) para identificar pontos críticos (breaking points). Na segunda, o *Project-Field-Explorer* aprofunda o estudo desses pontos e planeja as intervenções. Na terceira, o *Project-Evolution-Injector* aplica as correções de código geradas. Cada etapa é implementada como uma *skill* (habilidade) do Google Antigravity IDE.

As *Agent Skills* do Antigravity permitem estender as capacidades do agente de IA de forma modular. Cada skill é um diretório que contém um arquivo de definição SKILL.md com instruções específicas (além de scripts, referências e templates). No Google Antigravity, Skills são descritas como “um padrão aberto para estender as capacidades do agente” – essencialmente uma pasta contendo um SKILL.md. O Project Evolver Framework segue esse padrão: todas as suas funcionalidades são encapsuladas em skills instaláveis.

**Recursos Principais:**  
\- **Três Fases Analíticas:**  
\- *Project-Evolver-Mapper* (Mapeador) – Diagnóstico inicial: escaneia o projeto, deduz o propósito e identifica os “pontos de ruptura” (Breaking Points).  
\- *Project-Field-Explorer* (Explorador) – Pesquisa aprofundada: investiga cada ponto crítico, estima seu impacto (“raio de explosão”) e documenta os padrões associados.  
\- *Project-Evolution-Injector* (Injetor) – Correção automatizada: aplica as correções de arquitetura e código propostas, gerando um log de injeção (Injection Log) que lista mudanças efetuadas e salvaguardas mantidas.  
\- **Tecnologias Usadas:** Implementado em **Python** com instruções em **Markdown**. As skills usam scripts Python e arquivos de apoio (templates e referências em Markdown) para orientar o agente. O GitHub pode classificar o repositório como Python devido aos scripts, mas o foco está na lógica de IA e nas descrições em Markdown.  
\- **Integração com Antigravity:** Projetado para o ambiente Google Antigravity. As skills são carregadas sob demanda (ver Documentação Antigravity) para otimizar o contexto e evitar sobrecarga de informações.

### Instalação e Configuração

Para usar este framework, é necessário ter o [Google Antigravity IDE](https://antigravity.google) instalado. Em seguida:

* **Instale as Skills do Projeto:** Copie as pastas de cada skill (**project-evolver-mapper**, **project-field-explorer**, **project-evolution-injector**) para o diretório de skills do workspace:

* \<workspace-root\>/.agent/skills/project-evolver-mapper/    
  \<workspace-root\>/.agent/skills/project-field-explorer/    
  \<workspace-root\>/.agent/skills/project-evolution-injector/  

* Este é o escopo de workspace para skills. Ao colocar as pastas neste caminho, o Antigravity as reconhece como skills do projeto.

* **Estrutura do Repositório:** O repositório traz um diretório Skill Files/ com o conteúdo de cada skill (incluindo SKILL.md, scripts e arquivos de apoio). Não é necessário executar scripts manualmente; as ações são disparadas pelos prompts do agente.

* **Trigger (Ativação) das Skills:** Para acionar cada etapa, use as *trigger phrases* ou chame a skill diretamente no Antigravity. Por exemplo:

* @project-evolver-mapper – Inicia a análise do projeto. Comece pela **Entrevista de Visão Proativa** (fase de mapeamento).

* @project-field-explorer – Investiga os *Breaking Points* identificados no Mapa Global (fase de exploração).

* @project-evolution-injector – Implementa as correções descritas nos relatórios gerados (fase de injeção).

Essas frases devem ser inseridas como comandos ou prompts no editor do Antigravity. O agente então carrega a skill correspondente e executa suas instruções.

### Uso

1. **Mapeamento Inicial:** Após instalar as skills, abra o Antigravity e insira o comando para o *Mapper*:

* **Use** a habilidade @project-evolver-mapper e responda à *Entrevista de Visão Proativa*, confirmando o propósito do projeto. A skill irá criar/atualizar um arquivo GLOBAL\_MAP.md com a estrutura geral e pontos críticos.

2. **Pesquisa Detalhada:** Em seguida, inicie o *Explorer* com @project-field-explorer. Ele irá examinar cada ponto crítico do GLOBAL\_MAP.md, produzindo insights e indicando o *raio de impacto* das modificações. Os resultados são documentados em relatórios (ex.: FIELD\_RESEARCH\_REPORT.md).

3. **Aplicação de Correções:** Por fim, chame o *Injector* via @project-evolution-injector. A skill pede o relatório relevante (campo \[Report Names\]) e aplica as correções de código e arquitetura sugeridas. Um **Injection Log** é gerado, detalhando as alterações feitas e garantindo que regras-chave foram preservadas.

Sempre mantenha o GLOBAL\_MAP.md atualizado entre as etapas, para garantir que o agente tenha uma “fonte da verdade” arquitetural consistente.

### Licença e Autor

* **Licença:** MIT License (veja o arquivo LICENSE).

* **Autor:** Desenvolvido por Vitor (desenvolvedor solo) para facilitar a manutenção e evolução de código. Conforme recomendações do GitHub, incluímos informações de mantenedor e licença no README.

---

## English

**Description:** The Project Evolver Framework is a modular AI-driven system for systematically mapping, analyzing, and fixing structural bugs in software projects. It consists of **three stages** – *Mapper*, *Field Explorer*, and *Evolution Injector* – that together guide the project from diagnosis to automated refactoring. In the first stage, the **Project-Evolver-Mapper** skill performs a *Proactive Vision Interview* to scan the codebase, infer the project’s purpose, and identify “breaking points.” The second, **Project-Field-Explorer**, conducts deep research on these flaws and plans out the *blast radius* of each issue. The third, **Project-Evolution-Injector**, applies the proposed architectural and code fixes and records them in an injection log.

Each stage is implemented as a **Google Antigravity Agent Skill**. In Antigravity, skills are directory-based packages containing a SKILL.md instruction file (along with optional scripts, references, and templates). These Agent Skills are an *open standard* for extending an AI agent’s capabilities, each being “a folder containing a SKILL.md file”. The Project Evolver skills leverage this model to load only the needed instructions for each task, avoiding context overload.

**Key Features:**  
\- **Three-Phase Workflow:**  
\- *Project-Evolver-Mapper* – Initial codebase scan and vision interview (identifies core issues).  
\- *Project-Field-Explorer* – In-depth flaw analysis and solution planning.  
\- *Project-Evolution-Injector* – Automated code/architecture fixes and validation.  
\- **Technologies:** Implemented in **Python** with **Markdown**\-based prompts. The repository includes Python scripts and template files, but the high-level instructions are written in Markdown (hence GitHub may label it as 100% Python). The focus is on AI-guided logic rather than any specific language or framework.  
\- **Antigravity Integration:** These tools use Google Antigravity’s Agent Skills mechanism. Project-specific skills should be placed under the workspace’s .agent/skills/ directory so that Antigravity can detect and load them on demand. This keeps the agent’s context lean and efficient (only the relevant skill is loaded when needed).

### Installation and Setup

1. **Prerequisites:** Install the [Google Antigravity IDE](https://antigravity.google) and ensure it is properly configured.

2. **Add Project Skills:** Copy the skill folders into your workspace:

* \<workspace-root\>/.agent/skills/project-evolver-mapper/    
  \<workspace-root\>/.agent/skills/project-field-explorer/    
  \<workspace-root\>/.agent/skills/project-evolution-injector/  

* This follows the workspace-scope placement for skills. Once in place, the skills become available for that project.

3. **Repository Contents:** The repo contains a Skill Files/ directory with each skill’s full content (SKILL.md, scripts, and assets). You do not need to manually run these scripts; they are executed by the Antigravity agent when the skill is invoked.

### Usage

* **@project-evolver-mapper:** Use this trigger to start project analysis. Begin with the *Proactive Vision Interview*. The skill will prompt you to confirm the project’s purpose and then generate a GLOBAL\_MAP.md outlining the code structure and identified breaking points.

* **@project-field-explorer:** Use this to investigate the breaking points listed in GLOBAL\_MAP.md. It will research each issue in depth and suggest the scope of impact. Findings are written to a field research report (e.g., FIELD\_RESEARCH\_REPORT.md).

* **@project-evolution-injector:** Use this to apply the fixes described in the reports. Specify the relevant report ID when prompted, and the skill will perform the code injections and refactorings. Results are logged in an **Injection Log** (INJECTION\_LOG.md), which details modified files and ensures key safeguards are maintained.

Follow the sequence: map → explore → inject. Ensure the global map is updated after mapping and research phases so the agent has a consistent project overview. This README outlines exactly how to get started, in line with GitHub’s guidance on documenting usage and maintainers.

### License and Author

* **License:** MIT License (see LICENSE file).

* **Author:** Developed by Vitor (solo developer). As recommended, this README includes project ownership and usage information.

**References:** Project skills follow Google Antigravity’s documentation on Agent Skills. The skill definitions (SKILL.md) provide detailed step-by-step instructions for each phase. For more on Antigravity skills, see Google’s Agent Skills documentation.

---

