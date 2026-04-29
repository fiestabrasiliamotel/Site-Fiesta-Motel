import os
import re

html_content = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Fiesta Motel | Premium & Tech Experience</title>
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com" rel="preconnect"/>
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <link href="style.css" rel="stylesheet"/>
    <script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
</head>
<body>

    <!-- Ambient Glowing orbs for Tech Luxury Vibe -->
    <div class="ambient-glow glow-purple"></div>
    <div class="ambient-glow glow-dark"></div>

    <!-- Navigation -->
    <nav class="nav" id="nav">
        <a class="nav-logo" href="#">
            FIESTA <span class="title-stroke">MOTEL</span>
        </a>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#suites">Suítes Premium</a></li>
            <li><a href="cardapio.html">Cardápio</a></li>
            <li><a href="#experiencias">Experiências</a></li>
            <li><a href="#gastronomia">Gastronomia</a></li>
        </ul>
        <a class="nav-cta" href="#">Reservar Agora</a>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <!-- Video em Background Fullscreen -->
        <div class="hero-bg">
            <video id="hero-video" class="hero-video" playsinline muted preload="auto">
                <source src="file:///E:/Motel%20Fiesta/2026/Suite%20Premium%2010-20260323T174203Z-3-001/video_hero_scrub.mp4" type="video/mp4">
            </video>
            <div class="hero-overlay"></div>
        </div>

        <div class="hero-content">
            <div class="hero-tag">
                <div class="hero-tag-line"></div>
                <span class="hero-tag-text">Privacidade não é promessa. É projeto.</span>
            </div>
            <h1 class="hero-title">
                <span style="white-space: nowrap;">DO ESSENCIAL AO</span>
                <span class="title-stroke">EXTRAORDINÁRIO</span>
                <span>O AMBIENTE CERTO<br>PARA VOCÊ</span>
            </h1>
            <p class="hero-desc">
                Com estrutura planejada para máxima privacidade, o Fiesta oferece suítes que atendem diferentes momentos, combinando segurança, limpeza e ótimo custo-benefício.
            </p>
            <div class="hero-actions">
                <a class="btn-primary" href="#suites">
                    <span>Explorar Suítes</span>
                    <span class="iconify" data-icon="solar:arrow-right-linear"></span>
                </a>
            </div>
        </div>
    </section>

    <!-- Faixa preta para cobrir qualquer vazamento do vídeo na junção -->
    <div style="height:4px; background:#050505; position:relative; z-index:25; margin-top:-4px;"></div>

    <!-- Suites Section (Padrão Grid) -->
    <section class="suites" id="suites">
        <div class="suites-inner">
            <div class="suites-header reveal">
                <h2 class="section-title text-left mt-4" style="margin-bottom: 0;">SUÍTES<br/><span style="color: var(--accent-light);">EXCLUSIVAS</span></h2>
            </div>
            
            <div class="suites-grid">
                
                <!-- 1. Suíte Cinema -->
                <div class="suite-card reveal delay-100">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Cinema" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Su%C3%ADte%20Cinema%20-%2061-20260323T174027Z-3-001/Melhoradas/Foto%20panoramica%20cama%20cinema%2061.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 199 / 2H</div>
                        <h3 class="suite-title">Suíte Cinema</h3>
                        <p class="suite-desc">Tela de 150'', Home Theater e todos os streamings. Maratone seus favoritos de dentro da hidromassagem.</p>
                        <a class="btn-outline" href="suite-cinema.html">Detalhes</a>
                    </div>
                </div>

                <!-- 2. Suíte Premium -->
                <div class="suite-card reveal delay-200">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Premium" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Suite%20Premium%2010-20260323T174203Z-3-001/Melhoradas%20Premium%2010/SPA%20Premium%2010%205%20aconchegante.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 199 / 2H</div>
                        <h3 class="suite-title">Suíte Premium</h3>
                        <p class="suite-desc">Dois ambientes amplos, Smart TV 70'', hidromassagem e iluminação especial. Sofisticação sem abrir mão do conforto.</p>
                        <a class="btn-outline" href="suite-premium.html">Detalhes</a>
                    </div>
                </div>

                <!-- 3. Suíte Bali -->
                <div class="suite-card reveal delay-300">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Bali" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Suite%20Premium%2010-20260323T174203Z-3-001/Melhoradas%20Premium%2010/Suite%20Premium%2010%207.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 199 / 2H</div>
                        <h3 class="suite-title">Suíte Bali</h3>
                        <p class="suite-desc">Inspirada na Indonésia, combina rústico e relaxamento. Hidro nova, Smart TV com som e garagem privativa.</p>
                        <a class="btn-outline" href="suite-bali.html">Detalhes</a>
                    </div>
                </div>

                <!-- 4. Suíte Sado -->
                <div class="suite-card reveal delay-100">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Sado" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Suite%20Premium%2010-20260323T174203Z-3-001/Melhoradas%20Premium%2010/SPA%20Premium%2010%205%20aconchegante.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 199 / 2H</div>
                        <h3 class="suite-title">Suíte Sado</h3>
                        <p class="suite-desc">17m de cordas, balanço erótico, X de parede, jaula e guilhotina. Uma masmorra de luxo para explorar seus limites.</p>
                        <a class="btn-outline" href="suite-sado.html">Detalhes</a>
                    </div>
                </div>

                <!-- 5. Suíte Super Luxo -->
                <div class="suite-card reveal delay-200">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Super Luxo" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Suite%20Premium%2010-20260323T174203Z-3-001/Melhoradas%20Premium%2010/Suite%20Premium%2010%207.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 139 / 2H</div>
                        <h3 class="suite-title">Suíte Super Luxo</h3>
                        <p class="suite-desc">Hidromassagem, Smart TV, ar-condicionado e garagem privativa. Luxo e privacidade por um valor acessível.</p>
                        <a class="btn-outline" href="suite-super-luxo.html">Detalhes</a>
                    </div>
                </div>

                <!-- 6. Suíte Fiesta -->
                <div class="suite-card reveal delay-300">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Fiesta" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Su%C3%ADte%20Fiesta%2016-20260323T174126Z-3-001/Su%C3%ADte%20Fiesta%2016/Suite%20fiesta%20Tratadas/Suite%20FIesta%20Cama%20Horizontal%20escura%203.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 120 / 2H</div>
                        <h3 class="suite-title">Suíte Fiesta</h3>
                        <p class="suite-desc">A experiência assinatura do Fiesta Motel. Design exclusivo, tecnologia integrada e privacidade total em cada detalhe.</p>
                        <a class="btn-outline" href="suite-fiesta.html">Detalhes</a>
                    </div>
                </div>

                <!-- 7. Suíte Luxo -->
                <div class="suite-card reveal delay-100">
                    <div class="suite-img-wrapper">
                        <img alt="Suíte Luxo" class="suite-img" src="file:///E:/Motel%20Fiesta/2026/Su%C3%ADte%20Fiesta%2016-20260323T174126Z-3-001/Su%C3%ADte%20Fiesta%2016/Suite%20fiesta%20Tratadas/Suite%20FIesta%20Cama%20Horizontal%20escura%203.png"/>
                    </div>
                    <div class="suite-info">
                        <div class="suite-meta">A PARTIR DE R$ 89 / 2H</div>
                        <h3 class="suite-title">Suíte Luxo</h3>
                        <p class="suite-desc">Conforto e elegância com custo-benefício incomparável. Ideal para sair da rotina com qualidade e privacidade.</p>
                        <a class="btn-outline" href="suite-luxo.html">Detalhes</a>
                    </div>
                </div>
                
            </div>
        </div>
    </section>

    <!-- Gastronomia Section -->
    <section class="gastronomia" id="gastronomia">
        <div class="gastronomia-inner">
            <div style="text-align: center; margin-bottom: 4rem;" class="reveal">
                <h2 class="section-title">ALTA <span class="italic">GASTRONOMIA</span> 24H</h2>
                <p class="gastro-subtitle" style="margin-bottom: 0;">Descubra como o Fiesta proporciona um serviço de hotelaria completo com pratos deliciosos e drinks sofisticados a qualquer hora do dia ou da noite na privacidade da sua suíte.</p>
            </div>
            
            <div class="menu-grid">
                <div class="menu-col reveal">
                    <h3>Pratos Principais</h3>
                    <ul class="menu-list">
                        <li><span>Picadinho de Carne</span> <span class="price">R$ 49,90</span></li>
                        <li><span>Parmegiana de Frango</span> <span class="price">R$ 49,90</span></li>
                        <li><span>Parmegiana de Carne</span> <span class="price">R$ 68,00</span></li>
                        <li><span>Escalope ao Molho Madeira</span> <span class="price">R$ 69,90</span></li>
                        <li><span>Frango ao Laranja</span> <span class="price">R$ 59,90</span></li>
                        <li><span>Penne Basílico</span> <span class="price">R$ 59,90</span></li>
                    </ul>
                </div>
                <div class="menu-col reveal">
                    <h3>Bebidas & Drinks</h3>
                    <ul class="menu-list">
                        <li><span>Sucos Naturais</span> <span class="price">R$ 18,00</span></li>
                        <li><span>Cremes Tropicais</span> <span class="price">R$ 20,00</span></li>
                        <li><span>Caipirinha / Roska</span> <span class="price">R$ 25,00</span></li>
                    </ul>
                </div>
            </div>

            <div style="text-align: center; margin-top: 5rem;" class="reveal">
                <a class="btn-primary" href="cardapio.html">
                    <span class="iconify" data-icon="solar:menu-dots-square-linear" style="font-size: 1.2rem;"></span>
                    <span>Ver Cardápio Completo</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Experiências (Sex Shop / Avaliações) -->
    <section class="experiencias" id="experiencias">
        <div class="exp-grid">
            <div class="exp-card neon-border reveal">
                <h3 class="exp-title">Sex Shop <span class="italic">Oficial</span></h3>
                <p class="exp-desc">O catálogo erótico entregue com discrição na sua suíte. Acessórios (algemas, fantasias), linha de géis estimulantes, próteses e vibros.</p>
                <div style="margin-top:2rem">
                    <a class="service-link" href="#">Ver Catálogo <span class="iconify" data-icon="solar:arrow-right-linear"></span></a>
                </div>
            </div>
            <div class="exp-card neon-border reveal">
                <h3 class="exp-title">A Voz dos <span class="italic">Hóspedes</span></h3>
                <div class="review-item">
                    <p class="stars">★★★★★</p>
                    <p class="text">"O melhor de Brasília, fiquei encantado com a qualidade dos pratos e com a recepção."</p>
                </div>
                <div class="review-item">
                    <p class="stars">★★★★★</p>
                    <p class="text">"Suite linda, higienizada e automatizada. Luz, som e tv em um único controle."</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer reveal">
        <div class="footer-grid">
            <div class="footer-col brand">
                <a class="nav-logo" href="#" style="margin-bottom: 1rem; color: var(--white); text-shadow:none;">
                    FIESTA <span class="title-stroke">MOTEL</span>
                </a>
                <p>Sagocan BR-070 Km 05<br>Taguatinga Norte - Brasília</p>
            </div>
            <div class="footer-col">
                <h4>Contato</h4>
                <p>(61) 3372-6060 / 3372-7253</p>
                <p>WA: (61) 99282-7596</p>
                <p>atendimento@fiestamotel.com.br</p>
            </div>
            <div class="footer-col">
                <h4>Redes Sociais</h4>
                <a href="#" class="footer-link">Instagram</a>
                <a href="#" class="footer-link">Facebook</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Fiesta Brasília Motel. Todos os direitos reservados.</p>
        </div>
    </footer>

    <script>
        // Nav background appears ONLY after the exact 2500px pinning scroll of the hero
        const nav = document.getElementById('nav');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 2500) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });

        // Scroll Reveal Observer (from Gemini Design System params)
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: "0px 0px -50px 0px" });

        document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

        gsap.registerPlugin(ScrollTrigger);

        const video = document.getElementById('hero-video');
        if (video) video.load();

        // 1. HERO TRIGGER SÍNCRONO (Garante o pin-spacer de 2500px imediatamente)
        ScrollTrigger.create({
            trigger: ".hero",
            start: "top top",
            end: "+=2500", 
            pin: true,
            scrub: 0.1, 
            onUpdate: (self) => {
                if (video && video.duration) {
                    video.currentTime = self.progress * video.duration;
                }
            }
        });

        // 2. SUITES HORIZONTAL TRIGGER (Lido após o Hero, respeita o pin-spacer)
        const track = document.querySelector('.suites-grid');
        if (track) {
            function getScrollAmount() {
                // Matemática de translação estrita: Largura total do track menos a própria área de visão interna (suites-inner) + um pequeno respiro
                return Math.max(0, track.scrollWidth - document.querySelector('.suites-inner').clientWidth + 50); 
            }

            const tween = gsap.to(track, {
                x: () => -getScrollAmount(), // Anima ate o ultimo card
                ease: "none"
            });

            ScrollTrigger.create({
                trigger: ".suites",
                start: "top top",
                end: () => `+=${getScrollAmount()}`,
                pin: true,
                animation: tween,
                scrub: 1, 
                invalidateOnRefresh: true, 
            });
            
            // Força a fisica a reescanear a pagina APÓS todas as fotos pesarem e o width ser real
            window.addEventListener('load', () => {
                ScrollTrigger.refresh();
            });
        }
    </script>
</body>
</html>
"""

# Agora adicionamos o css do carrossel SEM alterar alturas e mantendo as classes corretas
carousel_css = """
    <style>
        .suite-img-carousel {
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scrollbar-width: none;
            -ms-overflow-style: none;
            height: 100%;
            width: 100%;
            scroll-behavior: smooth;
        }
        .suite-img-carousel::-webkit-scrollbar { display: none; }
        
        /* A imagem dentro do carrossel pega a classe .suite-img que já lida com width, height 100% e object-fit cover */
        .suite-img-carousel img.suite-img {
            flex: 0 0 100%;
            scroll-snap-align: start;
        }
        
        .carousel-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(5,5,5,0.6);
            border: 1px solid rgba(255,255,255,0.1);
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 10;
            transition: all 0.3s;
            opacity: 0;
        }
        .suite-img-wrapper:hover .carousel-btn {
            opacity: 1;
        }
        .carousel-btn:hover {
            background: rgba(157, 78, 221, 0.8);
        }
        .carousel-prev { left: 10px; }
        .carousel-next { right: 10px; }
        .carousel-dots {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 6px;
            z-index: 10;
        }
        .carousel-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            transition: all 0.3s;
        }
        .carousel-dot.active {
            background: var(--accent-light);
            transform: scale(1.3);
        }
    </style>
"""

html_content = html_content.replace("</head>", carousel_css + "\n</head>")

suites = {
    "Cinema": [
        r"E:\Motel Fiesta\2026\Suíte Cinema - 61-20260323T174027Z-3-001\Escolhodas para site",
        r"E:\Motel Fiesta\2026\Suíte Cinema 33-20260416T163233Z-3-001\Suíte Cinema 33"
    ],
    "Premium": [
        r"E:\Motel Fiesta\2026\Suite Premium 10-20260323T174203Z-3-001\Melhoradas Premium 10"
    ],
    "Bali": [
        r"E:\Motel Fiesta\2026\Suíte Bali 02-20260416T175525Z-3-001\Escolhidas para o Site"
    ],
    "Sado": [
        r"E:\Motel Fiesta\2026\Fotos Sado"
    ],
    "Super Luxo": [
        r"E:\Motel Fiesta\2026\Suíte Super Luxo Branca 52-20260416T163401Z-3-001\Super Luxo Branca Escolhida para o site",
        r"E:\Motel Fiesta\2026\Suite Super Luxo laranja 53-20260416T163437Z-3-001\Escolhidas Site",
        r"E:\Motel Fiesta\2026\Super Luxo Preta - 54-20260323T180317Z-3-001\Escolhidas Site"
    ],
    "Fiesta": [
        r"E:\Motel Fiesta\2026\Suíte Fiesta 16-20260323T174126Z-3-001\Escolhidas Site"
    ],
    "Luxo": [
        r"E:\Motel Fiesta\2026\Suíte Luxo-20260416T163326Z-3-001\Escolhidas Site"
    ]
}

def get_images(dirs, count=4):
    images = []
    for d in dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    path = os.path.join(d, f).replace("\\", "/")
                    images.append(f"file:///{path}")
                    if len(images) >= count:
                        return images
    return images

for suite_name, dirs in suites.items():
    images = get_images(dirs, count=4)
    if not images:
        continue
        
    imgs_html = ""
    for idx, img in enumerate(images):
        imgs_html += f'                            <img alt="Suíte {suite_name}" class="suite-img" src="{img}"/>\n'
        
    carousel_html = f"""<div class="suite-img-wrapper">
                        <button class="carousel-btn carousel-prev" onclick="scrollCarousel(this, -1)"><span class="iconify" data-icon="solar:alt-arrow-left-linear"></span></button>
                        <div class="suite-img-carousel" onscroll="updateDots(this)">
{imgs_html}                        </div>
                        <button class="carousel-btn carousel-next" onclick="scrollCarousel(this, 1)"><span class="iconify" data-icon="solar:alt-arrow-right-linear"></span></button>
                        <div class="carousel-dots">
                            {"".join(['<div class="carousel-dot' + (' active' if i==0 else '') + '"></div>' for i in range(len(images))])}
                        </div>
                    </div>"""
                    
    # Note que agora NÃO removemos a class="suite-img-wrapper" normal, ela se mantém!
    
    pattern = re.compile(rf'<div class="suite-img-wrapper">.*?</div>\s*<div class="suite-info">\s*<div class="suite-meta">[^<]+</div>\s*<h3 class="suite-title">Suíte {suite_name}</h3>', re.DOTALL)
    
    match = pattern.search(html_content)
    if match:
        old_part = match.group(0)
        new_part = re.sub(r'<div class="suite-img-wrapper">.*?</div>', carousel_html, old_part, flags=re.DOTALL)
        html_content = html_content.replace(old_part, new_part)

js_code = """
        function scrollCarousel(btn, dir) {
            const container = btn.parentElement.querySelector('.suite-img-carousel');
            const width = container.clientWidth;
            container.scrollBy({ left: dir * width, behavior: 'smooth' });
        }
        function updateDots(container) {
            const index = Math.round(container.scrollLeft / container.clientWidth);
            const dots = container.parentElement.querySelectorAll('.carousel-dot');
            dots.forEach((dot, i) => {
                if (i === index) dot.classList.add('active');
                else dot.classList.remove('active');
            });
        }
"""
html_content = html_content.replace("</body>", js_code + "\n</body>")

with open(r"E:\Motel Fiesta\2026\Site novo\index.html", 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Index reconstruído!")
