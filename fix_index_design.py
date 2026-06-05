import os
import re

site_dir = r"E:\Motel Fiesta\2026\Site novo"
index_path = os.path.join(site_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Remove the "03 Boutique" label from the sexshop section
# The user hated the "03 Boutique" section label because it wasn't requested.
# Let's replace the content of the Boutique section to be cleaner and match the original.
sexshop_start = index_html.find('<!-- Boutique Sensual (Sex Shop) -->')
sexshop_end = index_html.find('</section>', sexshop_start) + 10

if sexshop_start != -1 and sexshop_end != -1:
    new_sexshop = """    <!-- Boutique Sensual (Sex Shop) -->
    <section class="sexshop-section reveal" id="sexshop" style="background: var(--black); padding: 8rem 5rem; position: relative; border-top: 1px solid rgba(255,255,255,0.05); overflow: hidden;">
        <div class="ambient-glow glow-purple" style="top: 50%; left: 10%;"></div>
        <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; position: relative; z-index: 2;">
            <div class="sexshop-image" style="border-radius: 8px; overflow: hidden; position: relative;">
                <img src="assets/site_images/boutique_hero2.png" alt="Boutique Sensual" style="width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 8px;">
            </div>
            
            <div class="sexshop-content text-left">
                <span class="iconify" data-icon="solar:bag-heart-bold" style="font-size: 3.5rem; color: var(--accent-light); margin-bottom: 1.5rem; filter: drop-shadow(0 0 15px rgba(157,78,221,0.4));"></span>
                <h2 class="section-title text-left" style="margin-bottom: 1.5rem;">BOUTIQUE <span class="italic">SENSUAL</span></h2>
                <p style="color: var(--gray); font-size: 1.1rem; line-height: 1.8; margin-bottom: 2.5rem; font-weight: 300;">
                    Descubra nossa curadoria exclusiva de acessórios, géis e lingeries para elevar sua experiência a outro nível. Solicite com total discrição direto na sua suíte.
                </p>
                <a href="sexshop.html" class="btn-primary" style="background: var(--accent); border-color: var(--accent); color: var(--white); box-shadow: 0 0 20px rgba(157, 78, 221, 0.3); display: inline-flex;">
                    <span class="iconify" data-icon="solar:bag-heart-bold" style="font-size: 1.2rem;"></span>
                    <span>Explorar Catálogo</span>
                </a>
            </div>
        </div>
        
        <style>
            @media (max-width: 900px) {
                .sexshop-section > div { grid-template-columns: 1fr !important; text-align: center; }
                .sexshop-content.text-left { text-align: center; }
                .sexshop-content .section-title.text-left { text-align: center; font-size: 2.5rem !important; }
                .sexshop-section { padding: 4rem 2rem !important; }
                .sexshop-image { order: -1; margin-bottom: 2rem; max-height: 350px; }
            }
        </style>
    </section>"""
    index_html = index_html[:sexshop_start] + new_sexshop + index_html[sexshop_end:]

# 2. Replicate the EXACT booking section from suite-premium.html
# We must inject the CSS for `.booking-tagline` etc into the section or global style,
# and use the exact HTML.
booking_start = index_html.find('<!-- Nova Sessão de Reservas -->')
booking_end = index_html.find('</section>', booking_start) + 10

if booking_start != -1 and booking_end != -1:
    new_booking = """    <!-- Nova Sessão de Reservas -->
    <style>
        .booking-tagline {
            font-family: var(--serif); font-style: italic;
            font-size: clamp(1.5rem, 3vw, 2.5rem);
            color: var(--white-dim); margin-bottom: 3rem;
            line-height: 1.4;
        }
        .booking-tagline strong { font-style: normal; font-weight: 400; color: var(--accent-light); }
        .booking-actions { display: flex; align-items: center; justify-content: center; gap: 1.5rem; flex-wrap: wrap; }
        .btn-wpp {
            display: inline-flex; align-items: center; gap: 0.8rem;
            padding: 1rem 2.5rem;
            background: #075E54;
            color: #fff;
            font-size: 0.75rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase;
            border-radius: 2px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px rgba(7, 94, 84, 0.4);
            border: 1px solid #075E54;
        }
        .btn-wpp:hover { background: #128C7E; border-color: #128C7E; transform: translateY(-2px); box-shadow: 0 8px 30px rgba(7, 94, 84, 0.5); }
        .btn-phone {
            display: inline-flex; align-items: center; gap: 0.8rem;
            padding: 1rem 2.5rem;
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--white);
            font-size: 0.75rem; font-weight: 400; letter-spacing: 0.12em; text-transform: uppercase;
            border-radius: 2px;
            transition: all 0.3s ease;
        }
        .btn-phone:hover { border-color: rgba(255,255,255,0.3); background: rgba(255,255,255,0.03); }
        .booking-disclaimer { margin-top: 2rem; font-size: 0.72rem; color: var(--gray); }
        .booking-disclaimer strong { color: var(--accent-light); }
    </style>
    <section class="booking reveal" style="background: var(--black-card); padding: 8rem 2rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05);">
        <div style="max-width: 800px; margin: 0 auto;">
            <div class="section-label" style="justify-content: center; margin-bottom: 2rem;">
                <span class="section-label-num">04</span>
                <div class="section-label-line"></div>
                <span class="section-label-text">Reservas</span>
            </div>
            <p class="booking-tagline">
                Seu próximo momento especial<br>começa com <strong>uma mensagem</strong>.
            </p>
            <div class="booking-actions">
                <a class="btn-wpp" href="https://wa.me/556133726060?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." target="_blank">
                    <span class="iconify" data-icon="ic:baseline-whatsapp" style="font-size: 1.2rem;"></span>
                    Reservar via WhatsApp
                </a>
                <a class="btn-phone" href="tel:6133726060">
                    <span class="iconify" data-icon="solar:phone-bold" style="font-size: 1.2rem;"></span>
                    (61) 3372-6060
                </a>
            </div>
            <p class="booking-disclaimer">
                Pernoite das 23h às 06h (7h de duração) pelo preço de <strong>4 horas</strong>.<br>
                Entrada discreta com garagem privativa inclusa.
            </p>
        </div>
    </section>"""
    index_html = index_html[:booking_start] + new_booking + index_html[booking_end:]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("index.html fixed successfully!")
