import os
import re

site_dir = r"E:\Motel Fiesta\2026\Site novo"
sexshop_path = os.path.join(site_dir, "sexshop.html")

# Data from subagent
products = [
    {"name": "Bracelete", "price": "R$ 32,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.08-e1622055627118.jpeg"},
    {"name": "Calcinha", "price": "R$ 28,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.04-e1622055660888.jpeg"},
    {"name": "Fantasia sexy", "price": "R$ 80,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.05-1-e1622055708892.jpeg"},
    {"name": "Basic Gel", "price": "R$ 17,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.06-e1622055750247.jpeg"},
    {"name": "Give-in Gel", "price": "R$ 17,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.06-1-e1622055787994.jpeg"},
    {"name": "Suave in Gel", "price": "R$ 17,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.07-e1622055819777.jpeg"},
    {"name": "Prótese com vibrador", "price": "R$ 110,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.09-1-e1622055866160.jpeg"},
    {"name": "Prótese com cinta", "price": "R$ 95,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.08-1-e1622055903909.jpeg"},
    {"name": "Vibro Lady", "price": "R$ 50,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.09-e1622055940428.jpeg"},
    {"name": "Térmico INN", "price": "R$ 17,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.07-1-e1622055986877.jpeg"},
    {"name": "Sagocan", "price": "R$ 20,00", "image": "https://www.fiestamotel.com.br/wp-content/uploads/2021/05/WhatsApp-Image-2021-05-17-at-13.43.05-e1622056024185.jpeg"}
]

with open(sexshop_path, "r", encoding="utf-8") as f:
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

# Replace the content inside <div class="food-grid"> ... </div>
import re
new_html = re.sub(r'<div class="food-grid">.*?</div>\s*</section>', f'<div class="food-grid">\n{items_html}\n        </div>\n    </section>', html, flags=re.DOTALL)

with open(sexshop_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Images successfully added to sexshop.html!")
