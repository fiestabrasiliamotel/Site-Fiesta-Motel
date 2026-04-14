# 🏨 Novo Site Fiesta Motel - Descritivo do Projeto (System Prompt & Project Manifest)

## 📌 Visão Geral do Projeto
- **Nome do Projeto:** Novo Site Fiesta Motel
- **Objetivo:** Desenvolver uma interface web *premium*, imersiva e cinematográfica para o Fiesta Motel, superando as limitações dos templates antigos e construindo uma base de alto desempenho. O site deve transmitir exclusividade, luxo, prazer e vanguarda tecnológica.
- **Estado Atual:** Extração e refatoração de dados do site antigo/templates estruturais (arquivos de base do Framer). A interface está sendo lapidada com dados reais (quartos, valores, imagens tratadas). 

## 🎨 Identidade Visual e Estética (Design System Guidelines)
Qualquer Agente (IA) ou Desenvolvedor interagindo com este repositório **DEVE** seguir estas regras artísticas estritamente:
- **Tema Base:** Dark Mode absoluto. Fundos extremamente escuros (`#0B0B0E` a `#1A1A24`) e uso intensivo de Glassmorphism (fundos translúcidos sutis).
- **Tipografia:** 
  - *Títulos/Acentos:* Fontes Serifadas elegantes (como *Cinzel* ou *Crimson Text*) apenas para impacto heroico, ou *Sans-Serifs Premium* (como *Outfit* ou *Inter*) para peso institucional e limpo.
  - *Leitura Bruta:* *Inter* para máximo conforto com cores em alto contraste.
- **Paleta de Cores:**
  - Principal/Neutros: Preto absoluto ou quase preto, Branco vibrante e escalas de cinza/zinc.
  - Acentos (Accent): Violeta Luxuoso (`#9D4EDD` / `var(--accent-light)`) para destaques precisos, botões, ícones, gradientes de texto e preços. Fuga radical de genéricos.
- **Animações (Motion):** Suavidade em primeiríssimo lugar. Rolagens e revelações de conteúdo (`IntersectionObserver` nativo) devem ser contínuas e imersivas (curvas `cubic-bezier` longas). O uso de GSAP está previsto para *Scroll-Jacking* ou animações de linha do tempo complexas (Efeito Path), contudo **NUNCA DEVE QUEBRAR A ARQUITETURA NATIVA EM GRID**. Se houverem animações em carrosséis, devem respeitar `overflow-x: auto` e `scroll-snap` nativo sempre que o JavaScript falhar.
- **Imagens:** O material fotográfico e videográfico do usuário é contínuo e virá em etapas processadas (`E:\Motel Fiesta\2026\...`). Efeitos como imagem iniciar em preto/branco (grayscale 100%) no layout neutro e estourar em cores ricas no *hover* compõem nossa assinatura.

## ⚙️ Stack Tecnológico e Estrutura Atual
- **Stack Atual:** Vanilla JavaScript, HTML5 semântico, CSS puro modular (Variáveis nativas). 
- **Repositório Central:** `e:\Motel Fiesta\2026\Site novo\clearpath-template-framer-website\`
  - A pasta raiz engloba o que foi exportado dos moldes antigos.
  - Arquivos vivos geralmente trabalham na arquitetura do Vanilla.
- **Próximos Passos (Evolução):** Adequação integral dos assets para inserções de vídeos em autoplay (cenas do motel) e estruturação de novos catálogos (Sex Shop Integrado e Experiências) ainda não modelados.

## 🛡️ Regras de Ouro de Versionamento & IA (Workflow)
As IAs trabalhando neste projeto operam num sistema em tempo real na máquina do usuário (`Windows`, IDE `Cursor`), portanto as regras abaixo não são sugestões, são lei:
1. **Zero Destruição Não-Documentada:** Antes de aplicar qualquer ferramenta complexa ou mudança estrutural forte (como converter Grids para ScrollTrigger no GSAP), o agente DEVE assegurar via prompt que o repositório local está com o histórico em dia.
2. **Commit por Funcionalidade:** Implementamos Versionamento rigoroso no `Git`. Se você (IA) sugerir uma implantação grande, crie um passo lógico e engate um commit com a tag correspondente: `git commit -m "Nova Feature: XYZ"`.
3. **Paths de Assets:** Enquanto o setup final e as migrações absolutas não ocorrerem, o usuário poderá fornecer paths absolutos físicos (`file:///E:/Motel...`). O agente DEVE ser resiliente com esse tipo de src em HTML em fases de build pré-deploy comercial ativo.

## 📦 Entrega Futura de Materiais
- Novas integrações deverão respeitar e acomodar pesados Data Sets visuais, de forma lazy-loading (como tags de picture de loading eficiente) pois o projeto receberá baterias e *packs* fotográficos extensos recém-criados em 2026.
