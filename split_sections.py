import re

html_path = r"E:\Motel Fiesta\2026\Site novo\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

new_sections = """
    <!-- Boutique Sensual (Sex Shop) -->
    <section class="sexshop-section reveal" id="sexshop" style="background: var(--black-card); padding: 6rem 5rem; text-align: center; border-top: 1px solid rgba(157, 78, 221, 0.1);">
        <div class="dot-pattern"></div>
        <div style="max-width: 600px; margin: 0 auto; position: relative; z-index: 2;">
            <span class="iconify" data-icon="solar:bag-heart-bold" style="font-size: 3.5rem; color: var(--accent-light); margin-bottom: 1.5rem; filter: drop-shadow(0 0 15px rgba(157,78,221,0.4));"></span>
            <h2 class="section-title">BOUTIQUE <span class="italic">SENSUAL</span></h2>
            <p style="color: var(--gray); font-size: 1.05rem; line-height: 1.7; margin-bottom: 2.5rem;">
                Eleve sua experiência a outro nível. Solicite nosso catálogo erótico com total discrição direto na sua suíte. Trabalhamos com as melhores marcas, géis, acessórios e fantasias.
            </p>
            <a href="https://wa.me/5561992827596?text=Ol%C3%A1%21%20Gostaria%20de%20receber%20o%20cat%C3%A1logo%20do%20Sex%20Shop%20na%20minha%20su%C3%ADte." target="_blank" class="btn-primary" style="background: var(--accent); border-color: var(--accent); color: var(--white); box-shadow: 0 0 20px rgba(157, 78, 221, 0.3);">
                <span class="iconify" data-icon="ic:baseline-whatsapp" style="font-size: 1.2rem;"></span>
                <span>Solicitar Catálogo via WhatsApp</span>
            </a>
        </div>
    </section>

    <!-- Avaliações Google (A Voz dos Hóspedes) -->
    <section class="reviews-section" id="avaliacoes" style="padding: 6rem 0; overflow: hidden; position: relative; background: var(--black);">
        <div style="text-align: center; margin-bottom: 4rem; padding: 0 2rem;" class="reveal">
            <h2 class="section-title">A VOZ DOS <span class="italic">HÓSPEDES</span></h2>
            <div style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin-top: 1rem;">
                <span class="iconify" data-icon="logos:google-icon" style="font-size: 1.5rem;"></span>
                <span style="color: var(--white); font-weight: 500; font-size: 1.1rem;">5.0</span>
                <div style="color: #fbbc05; font-size: 1.2rem; letter-spacing: 2px;">★★★★★</div>
                <span style="color: var(--gray); font-size: 0.85rem; margin-left: 0.5rem;">Avaliações reais no Google Maps</span>
            </div>
        </div>
        
        <style>
            .reviews-carousel {
                display: flex;
                gap: 2rem;
                padding: 1rem 5rem 3rem;
                overflow-x: auto;
                scroll-snap-type: x mandatory;
                scrollbar-width: none;
                -ms-overflow-style: none;
            }
            .reviews-carousel::-webkit-scrollbar { display: none; }
            .review-card {
                min-width: 350px;
                max-width: 400px;
                background: rgba(17, 17, 24, 0.6);
                border: 1px solid rgba(255,255,255,0.05);
                padding: 2.5rem 2rem;
                border-radius: 8px;
                scroll-snap-align: center;
                flex-shrink: 0;
                transition: transform 0.3s ease, border-color 0.3s ease;
                position: relative;
            }
            .review-card:hover {
                transform: translateY(-5px);
                border-color: rgba(157, 78, 221, 0.3);
                background: rgba(17, 17, 24, 0.9);
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }
            .review-header {
                display: flex;
                align-items: center;
                gap: 1rem;
                margin-bottom: 1.5rem;
            }
            .reviewer-avatar {
                width: 45px; height: 45px;
                border-radius: 50%;
                background: var(--accent);
                display: flex; align-items: center; justify-content: center;
                color: var(--white); font-weight: 600; font-family: var(--sans);
                font-size: 1.2rem;
            }
            .reviewer-info h4 {
                color: var(--white); font-size: 0.95rem; font-weight: 500; margin-bottom: 0.2rem;
            }
            .reviewer-info .review-date {
                color: var(--gray); font-size: 0.75rem;
            }
            .review-stars { color: #fbbc05; font-size: 1.1rem; margin-bottom: 1.5rem; letter-spacing: 2px;}
            .review-text { color: var(--white-dim); font-size: 0.95rem; line-height: 1.6; font-style: italic; font-weight: 300; }
            .google-badge { position: absolute; top: 1.5rem; right: 1.5rem; font-size: 1.2rem; opacity: 0.7; }
            
            @media (max-width: 800px) {
                .reviews-carousel { padding: 1rem 2rem 3rem; }
                .review-card { min-width: 300px; padding: 1.5rem; }
            }
        </style>

        <div class="reviews-carousel reveal delay-200">
            <!-- Card 1 -->
            <div class="review-card">
                <span class="iconify google-badge" data-icon="logos:google-icon"></span>
                <div class="review-header">
                    <div class="reviewer-avatar" style="background: #4285F4;">M</div>
                    <div class="reviewer-info">
                        <h4>Marcos Silva</h4>
                        <div class="review-date">há 2 semanas</div>
                    </div>
                </div>
                <div class="review-stars">★★★★★</div>
                <p class="review-text">"O melhor de Brasília, fiquei encantado com a qualidade dos pratos e com a recepção. A suíte estava impecável e o serviço de quarto foi super rápido."</p>
            </div>
            <!-- Card 2 -->
            <div class="review-card">
                <span class="iconify google-badge" data-icon="logos:google-icon"></span>
                <div class="review-header">
                    <div class="reviewer-avatar" style="background: #0F9D58;">J</div>
                    <div class="reviewer-info">
                        <h4>Juliana C.</h4>
                        <div class="review-date">há 1 mês</div>
                    </div>
                </div>
                <div class="review-stars">★★★★★</div>
                <p class="review-text">"Suite linda, higienizada e automatizada. Luz, som e tv em um único controle. A hidromassagem é gigante e a iluminação deu um toque super especial à nossa noite."</p>
            </div>
            <!-- Card 3 -->
            <div class="review-card">
                <span class="iconify google-badge" data-icon="logos:google-icon"></span>
                <div class="review-header">
                    <div class="reviewer-avatar" style="background: #DB4437;">P</div>
                    <div class="reviewer-info">
                        <h4>Paulo R.</h4>
                        <div class="review-date">há 3 meses</div>
                    </div>
                </div>
                <div class="review-stars">★★★★★</div>
                <p class="review-text">"Comida maravilhosa, pratos super bem servidos e cardápio bem variado. Valeu muito a pena, atendimento nota 10 e total discrição desde a entrada até a saída."</p>
            </div>
            <!-- Card 4 -->
            <div class="review-card">
                <span class="iconify google-badge" data-icon="logos:google-icon"></span>
                <div class="review-header">
                    <div class="reviewer-avatar" style="background: #F4B400;">A</div>
                    <div class="reviewer-info">
                        <h4>Amanda T.</h4>
                        <div class="review-date">há 4 meses</div>
                    </div>
                </div>
                <div class="review-stars">★★★★★</div>
                <p class="review-text">"Conheci a Suíte Cinema e foi uma experiência indescritível! Assistimos a filmes comendo uns petiscos direto da banheira. Tudo limpinho, cheiroso e impecável."</p>
            </div>
            <!-- Card 5 -->
            <div class="review-card">
                <span class="iconify google-badge" data-icon="logos:google-icon"></span>
                <div class="review-header">
                    <div class="reviewer-avatar" style="background: #9d4edd;">C</div>
                    <div class="reviewer-info">
                        <h4>Carlos Eduardo</h4>
                        <div class="review-date">há 5 meses</div>
                    </div>
                </div>
                <div class="review-stars">★★★★★</div>
                <p class="review-text">"Instalações muito acima da média para o DF. A cama é super confortável e o ar condicionado gela de verdade. Preço muito justo pelo luxo entregue."</p>
            </div>
        </div>
    </section>
"""

# Regex para substituir a section antiga de experiencias inteira
pattern = re.compile(r'<!-- Experiências \(Sex Shop / Avaliações\) -->\s*<section class="experiencias".*?</section>', re.DOTALL)
new_html = pattern.sub(new_sections, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Seções de Sex Shop e Avaliações separadas com sucesso.")
