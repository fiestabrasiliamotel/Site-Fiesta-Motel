import os
import re
import shutil
import urllib.parse

# Paths
site_dir = r"E:\Motel Fiesta\2026\Site novo"
index_path = os.path.join(site_dir, "index.html")
cardapio_path = os.path.join(site_dir, "cardapio.html")
sexshop_path = os.path.join(site_dir, "sexshop.html")

# Image
generated_img_path = r"C:\Users\Raphael\.gemini\antigravity\brain\527d1e76-7f52-4f50-9ac8-902d246a36cb\boutique_hero_1777487249984.png"
dest_img_path = os.path.join(site_dir, "assets", "site_images", "boutique_hero.png")

if os.path.exists(generated_img_path):
    shutil.copy2(generated_img_path, dest_img_path)

# --- Update index.html ---
new_sexshop_section = """    <!-- Boutique Sensual (Sex Shop) -->
    <section class="sexshop-section reveal" id="sexshop" style="background: var(--black); padding: 8rem 5rem; position: relative; border-top: 1px solid rgba(255,255,255,0.05); overflow: hidden;">
        <div class="ambient-glow glow-purple" style="top: 50%; left: 10%;"></div>
        <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; position: relative; z-index: 2;">
            <div class="sexshop-image" style="border-radius: 8px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.8); position: relative;">
                <img src="assets/site_images/boutique_hero.png" alt="Boutique Sensual" style="width: 100%; height: 100%; object-fit: cover; display: block;">
                <div style="position: absolute; inset: 0; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; pointer-events: none;"></div>
            </div>
            
            <div class="sexshop-content text-left">
                <div class="section-label" style="margin-bottom: 1.5rem;">
                    <span class="section-label-num">03</span>
                    <div class="section-label-line"></div>
                    <span class="section-label-text">Boutique</span>
                </div>
                <h2 class="section-title text-left" style="font-size: 3rem; margin-bottom: 1.5rem;">BOUTIQUE <br><span class="italic" style="color: var(--accent-light);">SENSUAL</span></h2>
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
                .sexshop-content .section-label { justify-content: center; }
                .sexshop-section { padding: 4rem 2rem !important; }
                .sexshop-image { order: -1; margin-bottom: 2rem; max-height: 350px; }
            }
        </style>
    </section>"""

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = re.sub(
    r'<!-- Boutique Sensual \(Sex Shop\) -->.*?</section>', 
    new_sexshop_section, 
    index_html, 
    flags=re.DOTALL
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# --- Create sexshop.html ---
# We use cardapio as a base template, strip out the specific menu content, and put our sex shop items.
with open(cardapio_path, "r", encoding="utf-8") as f:
    cardapio_html = f.read()

# Replace head title
cardapio_html = cardapio_html.replace("<title>Cardápio | Fiesta Motel</title>", "<title>Boutique Sensual | Fiesta Motel</title>")

# Replace Page Header
new_header = """
    <header class="page-header" style="background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)), url('assets/site_images/boutique_hero.png') center/cover; padding: 12rem 2rem 6rem; text-align: center;">
        <h1 style="font-family: var(--serif); font-size: 4rem; font-weight: 400; color: var(--white); margin-bottom: 1rem; font-style: italic;">Boutique <span style="color: var(--accent-light);">Sensual</span></h1>
        <p style="color: var(--gray); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Pimenta e diversão na medida certa para a sua noite. Solicite qualquer item com total discrição direto para a sua suíte.</p>
    </header>
"""
cardapio_html = re.sub(r'<header class="page-header".*?</header>', new_header, cardapio_html, flags=re.DOTALL)

# Items
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

items_html = ""
for prod in products:
    wa_msg = urllib.parse.quote(f"Olá! Gostaria de pedir o item '{prod['name']}' do Sex Shop.")
    items_html += f"""
                <div class="menu-item reveal">
                    <div class="menu-item-content">
                        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
                            <h3 class="menu-item-title">{prod['name']}</h3>
                            <span class="menu-item-price" style="color: var(--accent-light); font-weight: 600; font-family: var(--serif); font-size: 1.2rem;">{prod['price']}</span>
                        </div>
                        <a href="https://wa.me/556133726060?text={wa_msg}" target="_blank" class="btn-pedir" style="margin-top: 1.5rem; display: inline-flex; align-items: center; gap: 0.5rem; background: transparent; border: 1px solid var(--accent); color: var(--accent-light); padding: 0.5rem 1rem; border-radius: 4px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s; text-decoration: none;">
                            <span class="iconify" data-icon="ic:baseline-whatsapp" style="font-size: 1.2rem;"></span>
                            Pedir via WhatsApp
                        </a>
                    </div>
                </div>
"""

new_menu_section = f"""
    <!-- Products Content -->
    <section class="menu-content" style="padding: 4rem 2rem; max-width: 1200px; margin: 0 auto;">
        
        <div class="menu-category" id="produtos" style="margin-top: 0; padding-top: 0;">
            <div class="category-header reveal">
                <h2>Todos os Produtos</h2>
                <div class="category-line"></div>
            </div>
            
            <div class="menu-grid">
                {items_html}
            </div>
        </div>

    </section>
"""

# Replace the entire menu section and categories navigation
cardapio_html = re.sub(r'<!-- Categorias Navigation -->.*?<!-- Footer -->', new_menu_section + "\n    <!-- Footer -->", cardapio_html, flags=re.DOTALL)

with open(sexshop_path, "w", encoding="utf-8") as f:
    f.write(cardapio_html)

print("Sex shop logic updated successfully!")
