import os
import shutil

site_dir = r"E:\Motel Fiesta\2026\Site novo"
index_path = os.path.join(site_dir, "index.html")
sexshop_path = os.path.join(site_dir, "sexshop.html")

# 1. Update the image
generated_img_path = r"C:\Users\Raphael\.gemini\antigravity\brain\527d1e76-7f52-4f50-9ac8-902d246a36cb\boutique_neon_1777487884109.png"
dest_img_path = os.path.join(site_dir, "assets", "site_images", "boutique_hero2.png")

if os.path.exists(generated_img_path):
    shutil.copy2(generated_img_path, dest_img_path)

# 2. Fix index.html
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Fix the image reference in Sex shop section
index_html = index_html.replace("assets/site_images/boutique_hero.png", "assets/site_images/boutique_hero2.png")

# Fix the Reservation CTA font
old_cta_title = '<h2 style="font-family: var(--serif); font-size: 3.5rem; font-weight: 400; font-style: italic; color: var(--white); line-height: 1.2; margin-bottom: 3rem;">'
new_cta_title = '<h2 class="section-title text-center" style="font-size: clamp(2rem, 4vw, 3rem); text-transform: uppercase; line-height: 1.2; margin-bottom: 3rem;">'
index_html = index_html.replace(old_cta_title, new_cta_title)

# Also fix the inner span of the CTA to match standard italic text style instead of weird gradient
old_cta_span = '<span style="background: linear-gradient(to right, #9d4edd, #ff79c6); -webkit-background-clip: text; color: transparent;">uma mensagem.</span>'
new_cta_span = '<span class="italic">uma mensagem.</span>'
index_html = index_html.replace(old_cta_span, new_cta_span)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# 3. Completely regenerate sexshop.html properly
sexshop_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Boutique Sensual | Fiesta Motel</title>
    
    <link href="https://fonts.googleapis.com" rel="preconnect"/>
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <link href="style.css" rel="stylesheet"/>
    <script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>

    <style>
        body { padding-top: 80px; }
        
        .menu-hero {
            text-align: center;
            padding: 5rem 2rem 3rem;
            position: relative;
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)), url('assets/site_images/boutique_hero2.png') center/cover;
            padding: 12rem 2rem 6rem;
        }
        .menu-hero h1 {
            font-family: var(--display);
            font-size: clamp(2.5rem, 5vw, 4rem);
            color: var(--white);
            margin-bottom: 1rem;
        }
        .menu-hero h1 .italic {
            font-weight: 600;
            color: var(--accent-light);
            text-shadow: 0 0 20px rgba(199, 125, 255, 0.4);
        }
        .menu-hero p {
            color: var(--gray-light);
            font-weight: 300;
            font-size: 1.1rem;
            max-width: 600px; 
            margin: 0 auto;
        }

        .menu-section {
            max-width: 1300px;
            margin: 4rem auto 6rem;
            padding: 0 3rem;
        }
        .menu-section-title {
            font-family: var(--display);
            font-size: 2.2rem;
            color: var(--white);
            margin-bottom: 2.5rem;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            padding-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .menu-section-title .iconify {
            color: var(--accent);
            font-size: 2.5rem;
        }

        .food-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2.5rem;
        }
        .food-card {
            background: rgba(28, 20, 39, 0.4);
            border: 1px solid rgba(157, 78, 221, 0.1);
            border-radius: 4px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: all 0.4s var(--ease-out-expo);
            backdrop-filter: blur(10px);
            padding: 2rem;
            align-items: center;
            text-align: center;
        }
        .food-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.4), 0 0 20px rgba(157, 78, 221, 0.15);
            border-color: rgba(199, 125, 255, 0.4);
        }
        .food-title {
            font-size: 1.3rem;
            color: var(--white);
            margin-bottom: 0.75rem;
            font-weight: 500;
        }
        .food-price {
            font-family: var(--sans);
            font-size: 1.5rem;
            color: var(--accent-light);
            font-weight: 600;
            margin-bottom: 1.5rem;
        }
        .btn-add {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            padding: 0.8rem 1.5rem;
            border: 1px solid var(--accent);
            color: var(--accent-light);
            background: rgba(157, 78, 221, 0.05);
            transition: all 0.3s;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        .btn-add:hover {
            background: var(--accent);
            color: var(--white);
            box-shadow: 0 0 15px rgba(157, 78, 221, 0.4);
        }

        @media (max-width: 1000px) {
            .menu-section { padding: 0 2rem; }
            .food-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav class="nav scrolled" id="nav" style="background: rgba(5,5,5,0.95); padding: 1rem 3rem;">
        <a class="nav-logo" href="index.html">
            FIESTA <span class="title-stroke">MOTEL</span>
        </a>
        <ul class="nav-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="index.html#suites">Suítes</a></li>
            <li><a href="cardapio.html">Cardápio</a></li>
        </ul>
        <a class="nav-cta" href="https://wa.me/556133726060?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." target="_blank">Reservar Agora</a>
    </nav>

    <!-- Hero -->
    <div class="menu-hero">
        <h1>BOUTIQUE <span class="italic">SENSUAL</span></h1>
        <p>Pimenta e diversão na medida certa para a sua noite. Solicite qualquer item com total discrição direto para a sua suíte.</p>
    </div>

    <!-- Products -->
    <section class="menu-section">
        <h2 class="menu-section-title">
            <span class="iconify" data-icon="solar:bag-heart-bold"></span> Todos os Produtos
        </h2>
        <div class="food-grid">
"""

products = [
  {"name": "Bracelete", "price": "R$ 32,00"},
  {"name": "Calcinha", "price": "R$ 28,00"},
  {"name": "Fantasia sexy", "price": "R$ 80,00"},
  {"name": "Basic Gel", "price": "R$ 17,00"},
  {"name": "Give-in Gel", "price": "R$ 17,00"},
  {"name": "Suave in Gel", "price": "R$ 17,00"},
  {"name": "Prótese com vibrador", "price": "R$ 110,00"},
  {"name": "Prótese com cinta", "price": "R$ 95,00"},
  {"name": "Vibro Lady", "price": "R$ 50,00"},
  {"name": "Térmico INN", "price": "R$ 17,00"}
]

import urllib.parse
for prod in products:
    wa_msg = urllib.parse.quote(f"Olá! Estou na suíte e gostaria de pedir o item do Sex Shop: {prod['name']}")
    sexshop_content += f"""
            <div class="food-card reveal">
                <h3 class="food-title">{prod['name']}</h3>
                <div class="food-price">{prod['price']}</div>
                <a href="https://wa.me/556133726060?text={wa_msg}" target="_blank" class="btn-add">
                    <span class="iconify" data-icon="ic:baseline-whatsapp" style="font-size: 1.2rem;"></span>
                    Pedir via WhatsApp
                </a>
            </div>
"""

sexshop_content += """
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer" style="padding-top: 3rem;">
        <div class="footer-bottom">
            <p>&copy; 2026 Fiesta Brasília Motel. Todos os direitos reservados.</p>
        </div>
    </footer>
    
    <script>
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    </script>
</body>
</html>
"""

with open(sexshop_path, "w", encoding="utf-8") as f:
    f.write(sexshop_content)

print("Fixed successfully!")
