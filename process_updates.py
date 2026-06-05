import os
import re
import urllib.parse

site_dir = r"E:\Motel Fiesta\2026\Site novo"

# 1. Update Navigation Block globally
# The generic nav we want:
new_nav = '''    <nav class="nav" id="nav">
        <a class="nav-logo" href="index.html#home">
            FIESTA <span class="title-stroke">MOTEL</span>
        </a>
        <ul class="nav-links">
            <li><a href="index.html#home">Home</a></li>
            <li><a href="index.html#suites">Suítes</a></li>
            <li><a href="cardapio.html">Cardápio</a></li>
        </ul>
        <a class="nav-cta" href="https://wa.me/556133726060?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." target="_blank">Reservar Agora</a>
    </nav>'''

# Reservation CTA HTML to add before Footer
reservations_cta = '''
    <!-- Nova Sessão de Reservas -->
    <section class="reservations-cta reveal" style="background: var(--black-card); padding: 8rem 2rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05);">
        <div style="max-width: 800px; margin: 0 auto;">
            <div class="section-label" style="justify-content: center; margin-bottom: 2rem;">
                <span class="section-label-num">04</span>
                <div class="section-label-line"></div>
                <span class="section-label-text">Reservas</span>
            </div>
            <h2 style="font-family: var(--serif); font-size: 3.5rem; font-weight: 400; font-style: italic; color: var(--white); line-height: 1.2; margin-bottom: 3rem;">
                Seu próximo momento especial<br>começa com <span style="background: linear-gradient(to right, #9d4edd, #ff79c6); -webkit-background-clip: text; color: transparent;">uma mensagem.</span>
            </h2>
            <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
                <a href="https://wa.me/556133726060?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." target="_blank" class="btn-primary" style="background: #115e59; border-color: #115e59; padding: 1.2rem 2.5rem; border-radius: 4px; color: var(--white); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; display: flex; align-items: center; gap: 0.8rem; transition: transform 0.3s ease;">
                    <span class="iconify" data-icon="ic:baseline-whatsapp" style="font-size: 1.4rem;"></span>
                    Reservar via WhatsApp
                </a>
                <a href="tel:6133726060" class="btn-outline" style="border-color: rgba(255,255,255,0.1); color: var(--white); padding: 1.2rem 2.5rem; border-radius: 4px; font-weight: 600; display: flex; align-items: center; gap: 0.8rem; background: rgba(0,0,0,0.2);">
                    <span class="iconify" data-icon="ic:baseline-phone" style="font-size: 1.4rem;"></span>
                    (61) 3372-6060
                </a>
            </div>
            <p style="color: var(--gray); font-size: 0.95rem; margin-top: 3rem; line-height: 1.6;">
                Pernoite das 23h às 06h (7h de duração) pelo preço de <strong style="color: var(--accent-light);">4 horas</strong>.<br>
                Entrada discreta com garagem privativa inclusa.
            </p>
        </div>
    </section>
'''

html_files = [f for f in os.listdir(site_dir) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(site_dir, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Update Navigation
    content = re.sub(r'<nav class="nav" id="nav">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    # Check if index.html to do specific updates
    if filename == 'index.html':
        # 2. Update the "SUÍTES EXCLUSIVAS" title
        content = content.replace(
            '<h2 class="section-title text-left mt-4" style="margin-bottom: 0;">SUÍTES<br/><span style="color: var(--accent-light);">EXCLUSIVAS</span></h2>',
            '<h2 class="section-title text-center" style="margin-bottom: 3rem;">SUÍTES <span class="italic">EXCLUSIVAS</span></h2>'
        )
        
        # 3. Update ScrollTrigger for smoother pinned scroll
        old_scroll = '''            ScrollTrigger.create({
                trigger: ".suites",
                start: "top top",
                end: () => `+=${getScrollAmount()}`,
                pin: true,
                animation: tween,
                scrub: 1, 
                invalidateOnRefresh: true, 
            });'''
        new_scroll = '''            ScrollTrigger.create({
                trigger: ".suites",
                start: "top top",
                end: () => `+=${getScrollAmount()}`,
                pin: true,
                animation: tween,
                scrub: 1.5,
                anticipatePin: 1,
                invalidateOnRefresh: true, 
            });'''
        content = content.replace(old_scroll, new_scroll)
        
        # 4. Add Reservation CTA before Footer
        if 'Nova Sessão de Reservas' not in content:
            content = content.replace('<!-- Footer -->', reservations_cta + '\n    <!-- Footer -->')

    # 5. Fix suite-specific whatsapp links
    if filename.startswith('suite-'):
        # extract suite name
        suite_name = filename.replace('suite-', '').replace('.html', '').replace('-', ' ').title()
        # map back to actual display name
        if suite_name == 'Super Luxo': suite_name = 'Suíte Super Luxo'
        elif suite_name == 'Fiesta': suite_name = 'Suíte Fiesta'
        elif suite_name == 'Premium': suite_name = 'Suíte Premium'
        elif suite_name == 'Cinema': suite_name = 'Suíte Cinema'
        elif suite_name == 'Bali': suite_name = 'Suíte Bali'
        elif suite_name == 'Sado': suite_name = 'Suíte Sado'
        elif suite_name == 'Luxo': suite_name = 'Suíte Luxo'
        
        encoded_correct = urllib.parse.quote(f"Olá! Gostaria de reservar a {suite_name}")
        encoded_wrong1 = urllib.parse.quote("Olá! Gostaria de reservar a Suíte Premium")
        encoded_wrong2 = urllib.parse.quote("Olá! Gostaria de reservar a Suíte Fiesta") # just in case
        
        content = content.replace(encoded_wrong1, encoded_correct)
        content = content.replace(encoded_wrong2, encoded_correct)
        
        # also check if the text visible on screen says "Suíte Premium" inside the button itself
        # some might have `<span style="font-weight: 500;">Suíte Premium</span>`
        content = re.sub(
            r'Reservar\s*<span[^>]*>(Suíte\s*Premium|Suíte\s*Fiesta)</span>',
            f'Reservar <span style="font-weight: 500;">{suite_name}</span>',
            content,
            flags=re.IGNORECASE
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates completed successfully.")
