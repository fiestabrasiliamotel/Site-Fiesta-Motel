import os
import shutil

site_dir = r"E:\Motel Fiesta\2026\Site novo"
assets_dir = os.path.join(site_dir, "assets", "sexshop")
sexshop_path = os.path.join(site_dir, "sexshop.html")

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

# Copy the 3 generated images
img_lingerie = r"C:\Users\Raphael\.gemini\antigravity\brain\527d1e76-7f52-4f50-9ac8-902d246a36cb\lingerie_sexshop_1777500847004.png"
img_gel = r"C:\Users\Raphael\.gemini\antigravity\brain\527d1e76-7f52-4f50-9ac8-902d246a36cb\gel_sexshop_1777500859736.png"
img_acessorio = r"C:\Users\Raphael\.gemini\antigravity\brain\527d1e76-7f52-4f50-9ac8-902d246a36cb\acessorio_sexshop_1777500874439.png"

shutil.copy2(img_lingerie, os.path.join(assets_dir, "lingerie.png"))
shutil.copy2(img_gel, os.path.join(assets_dir, "gel.png"))
shutil.copy2(img_acessorio, os.path.join(assets_dir, "acessorio.png"))

products = [
    {"name": "Bracelete", "price": "R$ 32,00", "image": "assets/sexshop/acessorio.png"},
    {"name": "Calcinha", "price": "R$ 28,00", "image": "assets/sexshop/lingerie.png"},
    {"name": "Fantasia sexy", "price": "R$ 80,00", "image": "assets/sexshop/lingerie.png"},
    {"name": "Basic Gel", "price": "R$ 17,00", "image": "assets/sexshop/gel.png"},
    {"name": "Give-in Gel", "price": "R$ 17,00", "image": "assets/sexshop/gel.png"},
    {"name": "Suave in Gel", "price": "R$ 17,00", "image": "assets/sexshop/gel.png"},
    {"name": "Prótese com vibrador", "price": "R$ 110,00", "image": "assets/sexshop/acessorio.png"},
    {"name": "Prótese com cinta", "price": "R$ 95,00", "image": "assets/sexshop/acessorio.png"},
    {"name": "Vibro Lady", "price": "R$ 50,00", "image": "assets/sexshop/acessorio.png"},
    {"name": "Térmico INN", "price": "R$ 17,00", "image": "assets/sexshop/gel.png"},
    {"name": "Sagocan", "price": "R$ 20,00", "image": "assets/sexshop/gel.png"}
]

with open(sexshop_path, 'r', encoding='utf-8') as f:
    html = f.read()

import urllib.parse
items_html = ""
for prod in products:
    wa_msg = urllib.parse.quote(f"Olá! Estou na suíte e gostaria de pedir o item do Sex Shop: {prod['name']}")
    items_html += f"""
            <div class="food-card reveal" style="padding: 0; align-items: stretch; text-align: left;">
                <div style="height: 250px; overflow: hidden; width: 100%; position: relative;">
                    <img src="{prod['image']}" alt="{prod['name']}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div style="padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1;">
                    <h3 class="food-title" style="margin-bottom: 0.5rem; font-size: 1.2rem;">{prod['name']}</h3>
                    <div class="food-price" style="margin-bottom: 1.5rem; font-size: 1.1rem;">{prod['price']}</div>
                    <div style="margin-top: auto;">
                        <a href="https://wa.me/556133726060?text={wa_msg}" target="_blank" class="btn-add" style="width: 100%; justify-content: center;">
                            <span class="iconify" data-icon="ic:baseline-whatsapp" style="font-size: 1.2rem;"></span>
                            Pedir via WhatsApp
                        </a>
                    </div>
                </div>
            </div>
"""

import re
new_html = re.sub(r'<div class="food-grid">.*?</div>\s*</section>', f'<div class="food-grid">\n{items_html}\n        </div>\n    </section>', html, flags=re.DOTALL)

with open(sexshop_path, "w", encoding="utf-8") as f:
    f.write(new_html)
