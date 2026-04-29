# Design System: Fiesta Motel — Site Institucional

> Gerado pela skill `design-md` com base na análise dos arquivos `style.css` e `suite-premium.html` do projeto.

---

## 1. Visual Theme & Atmosphere

**Tom geral:** Noturno, sensual e contido. O site respira escuridão de luxo — não é negro chapado, mas um preto com alma roxa, como uma sala VIP iluminada por luz violeta ambiente. A experiência visual é **cinematográfica e imersiva**: o vídeo hero domina sem pedir licença, e as seções emergem como cenas que se revelam no scroll.

**Filosofia estética:** "Dark Luxury" — a privacidade e o prazer comunicados através da ausência de ruído visual. O branco existe apenas como elemento tipográfico de contraste. O luxo não grita; ele sussurra em roxo neon.

**Densidade:** Deliberadamente espaçosa. Margens generosas (`8rem` de padding vertical nas seções principais) criam silêncio visual entre os elementos — cada bloco tem espaço para respirar e ser absorvido.

**Personalidade:** Sedutora, confiante, discreta. Nunca exuberante, nunca básica.

---

## 2. Color Palette & Roles

### Fundação

| Nome Semântico | Hex | Variável CSS | Papel Funcional |
|---|---|---|---|
| **Abismo Noturno** | `#050505` | `--black` | Background principal de todas as seções. Preto quase absoluto com leve tint. |
| **Preto Roxo Profundo** | `#100b16` | `--black-light` | Backgrounds alternativos, cards secundários. Preto com alma roxa visível. |
| **Roxo Lunar** | `#1c1427` | `--black-medium` | Usado em gradientes de fundo, overlay de seções de contraste. |

### Acento Principal — A Assinatura Visual

| Nome Semântico | Hex | Variável CSS | Papel Funcional |
|---|---|---|---|
| **Ametista Profunda** | `#9d4edd` | `--accent` | Cor de marca. Usada em bordas, ícones ativos, glows ambiente e elementos decorativos de identidade. |
| **Neon Violeta** | `#c77dff` | `--accent-light` | Tipografia de destaque, tags de texto ("SUÍTES EXCLUSIVAS"), spans em títulos de seção, hover states. É a cor que o olho encontra primeiro. |
| **Vinhedo Escuro** | `#5a189a` | `--accent-dark` | Glow de fundo difuso (fixed, blur 140px). Cria atmosfera sem chamar atenção. |

### Acento Secundário — Luxo Dourado (suite-premium.html)

| Nome Semântico | Hex | Variável CSS | Papel Funcional |
|---|---|---|---|
| **Ouro Envelhecido** | `#c9a84c` | `--gold` | CTAs primários de reserva. Botão dourado sinaliza ação de valor máximo. |
| **Champagne Iluminado** | `#e8c97a` | `--gold-light` | Hover dos botões dourados, preços em destaque nas tabelas de pricing. |

### Tipografia & Neutros

| Nome Semântico | Hex | Variável CSS | Papel Funcional |
|---|---|---|---|
| **Branco Puro** | `#ffffff` | `--white` | Títulos principais, texto de corpo sobre fundo escuro. |
| **Branco Lilás** | `#e0dced` | `--white-dim` | Subtítulos, textos de apoio de hierarquia secundária. Suave versus o branco puro. |
| **Cinza Roxo** | `#827b93` | `--gray` | Metadados, labels, textos de apoio. Legível mas hierarquicamente submisso. |
| **Cinza Claro** | `#a39eb5` | `--gray-light` | Textos descritivos, preços secundários, breadcrumbs. |

---

## 3. Typography Rules

### Famílias Tipográficas

**Fonte Principal — Outfit**
- Variável: `--sans` / `--display`
- Caráter: Geométrica moderna, limpa, excelente em peso leve. Funciona tanto em `200` (ultra leve, etéreo) quanto em `600` (assertivo, âncora).
- Usos: Navegação, botões, metadados, body text, títulos principais em caixa alta.

**Fonte Secundária — Playfair Display** *(Page de suíte)*
- Variável: `--serif`
- Caráter: Elegância editorial, nuances de serif clássica com personalidade contemporânea. O uso em itálico é característico.
- Usos: Subtítulos em itálico, citações, taglines de seção ("*Sofisticação em dois ambientes únicos*"), elementos que precisam de calor e humanidade.

**Fonte de Apoio Original — Cinzel** *(index.html)*
- Variável: `--serif` (fallback)
- Caráter: Serifa clássica romana, majestosa em caixa alta.
- Usos: Títulos de seção em caixa alta no site principal.

### Hierarquia Tipográfica

```
Hero Title:        clamp(2.5rem → 5rem)   | weight: 200-300 | letter-spacing: 0.02em
Section Title:     clamp(2rem → 4rem)      | weight: 200     | serif/sans mix
Suite Title:       1.25rem                 | weight: 500     | sans
Nav Logo:          1.5rem                  | weight: 600     | letter-spacing: 0.25em
Tag/Label:         0.65–0.8rem             | weight: 300-700 | letter-spacing: 0.2–0.35em | UPPERCASE
Body:              0.85–1rem               | weight: 300     | line-height: 1.6–1.8
Price Display:     1.8rem                  | weight: 300     | cinematic, minimal
```

### Regras de Uso

- **Caixa alta com letter-spacing generoso** é a linguagem dos labels e metadados. Nunca usar em parágrafos.
- **Pesos finos (`200`, `300`)** dominam os títulos grandes — o luxo é silencioso, não pesado.
- **Itálico da Playfair** é reservado para momentos de calor e intimidade (subtítulos de página de suíte, taglines de reserva).
- **Nunca** misturar Cinzel com letras minúsculas — ela existe apenas em UPPERCASE.

---

## 4. Component Stylings

### Botões

**Botão Primário — CTA de Reserva (Dourado)**
- Forma: Bordas levemente quadradas (`border-radius: 2px`) — não é pill, não é sharp. É uma escolha deliberada de refinamento geométrico.
- Background: Gradiente diagonal `#c9a84c → #e8c97a`
- Texto: Preto profundo `#1a1000` — máximo contraste em fundo quente
- Sombra: `0 4px 20px rgba(201,168,76,0.3)` em repouso → `0 8px 30px rgba(201,168,76,0.5)` no hover
- Hover: `translateY(-2px)` + sombra expandida — flutuação sutil de vida

**Botão Secundário — Outline Suave**
- Forma: `border-radius: 50px` (pill) — contraste intencional com o botão primário quadrado
- Background: `transparent` com `border: 1px solid rgba(255,255,255,0.1)`
- Texto: Branco puro
- Hover: `background: rgba(255,255,255,0.05)` + border levemente mais brillante

**Botão WhatsApp**
- Forma: `border-radius: 2px` (quadrado, igual ao primário)
- Background: `#075E54` (verde WhatsApp oficial)
- Hover: `#128C7E` + `translateY(-2px)`

### Cards de Suíte

- **Dimensões:** Largura fixa de `340px` (desktop), altura flexível
- **Imagem:** `190px` de altura, `object-fit: cover`, com overlay gradiente de baixo para cima
- **Info Area:** Background `rgba(11,11,14,1)` — quase preto, levemente diferente do fundo para criar separação sutil
- **Borda:** `1px solid rgba(255,255,255,0.05)` em repouso → `rgba(157,78,221,0.4)` no hover
- **Hover:** `translateY(-10px)` — elevação dramática como cartão sendo apresentado
- **Bordas arredondadas:** `border-radius: 4px` — mínimas, quase imperceptíveis

### Cards de Preço

- Forma: Sem border-radius (sharp edges) — assertividade, comunicação direta de valor
- Background: `var(--black-card)` = `#111118`
- Topo: Barra de `2px` no topo — roxo (`--accent`) para padrão, dourado para featured
- Hierarquia interna: Label de período → Dias → Linhas de preço (duração + valor)

### Divisor Decorativo (Losango)

- Elemento de identidade único: `div` de `6px × 6px` rotacionado `45deg`
- Cor: `var(--accent)` com `box-shadow: 0 0 10px var(--accent)` (glow)
- Flanqueado por linhas horizontais `rgba(255,255,255,0.06)`
- Aparece entre todas as seções da página de suíte — cria ritmo visual pulsante

### Tags de Seção (Numeração)

```
[ 01 ]——————[ COMODIDADES ]
```
- Número em `--accent`, weight 700, letter-spacing 0.2em
- Linha curta de 30px em `--accent` com 50% de opacity
- Texto em `--gray`, letra-spacing 0.25em, uppercase
- Cria hierarquia narrativa tipo editorial de revista de arquitetura

---

## 5. Layout Principles

### Grid e Espaçamento

- **Seção padrão:** `padding: 8rem 5rem` — espaço interno muito generoso, comunicando premium
- **Max-width:** `1400px` para conteúdo principal; `1000px` para gastronomia
- **Suites grid:** `display: flex`, `gap: 24px`, `overflow: hidden` com scroll horizontal por GSAP
- **Amenidades grid:** `grid-template-columns: repeat(4, 1fr)`, separação por `gap: 2px` — quase que fundidos, formando um bloco unitário

### Camadas de Z-Index

```
Nav:           z-index 1000  (sempre no topo)
Hero Content:  z-index 10
Hero Overlay:  z-index 5
Hero BG:       z-index 0
Suites:        z-index 20   (sobrepõe o pin-spacer da hero)
Lightbox:      z-index 1000
```

### Padrão de Scroll

- **Hero:** pinada por GSAP ScrollTrigger durante 2500px de scroll virtual
- **Suítes:** scroll horizontal nativo via GSAP (grid desliza lateralmente)
- **Resto:** scroll vertical padrão com `.reveal` animations (IntersectionObserver)

### Reveal Animations

- Todos os elementos de conteúdo entram com `opacity: 0 → 1` + `translateY(40px → 0)`
- Duração: `0.9s` com `cubic-bezier(0.16, 1, 0.3, 1)` (Expo Out — rápido no início, suavíssimo no final)
- Threshold: `0.1` — dispara ao primeiro pixel visível
- rootMargin: `-60px` — aguarda um pouco mais antes de revelar

### Textura & Profundidade

- **Dot Pattern:** `radial-gradient` de `1px` a cada `30px` — textura pontilhada quase invisível nas seções escuras
- **Ambient Text:** Texto gigante (`6rem → 16rem`) com `-webkit-text-stroke: 1px rgba(255,255,255,0.03)` — profundidade sem peso visual
- **Glows fixos:** Duas esferas roxas desfocadas (`blur: 140px`) no background fixo — criam atmosfera violeta ambiente na página inteira

---

## 6. Motion & Interaction Principles

- **Filosofia:** Tudo responde, nada surpreende. As transições são suaves e previsíveis.
- **Hover padrão:** `0.3–0.4s ease` — nunca instantâneo, nunca lento
- **Elevação em hover:** Botões e cards "flutuam" com `translateY(-2px a -10px)` — comunicam que são clicáveis de forma elegante
- **Imagens em hover:** Zoom lento `scale(1.05–1.06)` em `0.6–0.8s` — câmera lenta cinematográfica
- **Nav ao scroll:** `backdrop-filter: blur(20px)` aparece + borda roxa sutil — transição de transparente para sólido em `0.4s`

---

## 7. Identity Markers — O que faz o Fiesta ser o Fiesta

1. **O losango roxo brilhante** entre seções — elemento geométrico de assinatura
2. **Numeração editorial de seções** `[ 01 ]` com linha e label
3. **Texto ambiente gigantesco** em ghost stroke (`#fff` com 3% opacity)
4. **Fontes leves em títulos grandes** — o peso visual vem do tamanho, não do boldness
5. **Neon Violeta (`#c77dff`)** sempre presente nos destaques e spans de título
6. **Gradiente inferior nas imagens** de suíte — sempre `rgba(11,11,14,1) → transparent`
7. **Pill vs Quadrado** — contraste intencional entre botões secundários (pill) e primários (quadrado)
