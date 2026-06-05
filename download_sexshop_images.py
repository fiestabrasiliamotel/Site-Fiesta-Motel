import os
import urllib.request
import re

site_dir = r"E:\Motel Fiesta\2026\Site novo"
assets_dir = os.path.join(site_dir, "assets", "sexshop")
sexshop_path = os.path.join(site_dir, "sexshop.html")

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

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

with open(sexshop_path, 'r', encoding='utf-8') as f:
    html = f.read()

for prod in products:
    url = prod['image']
    filename = url.split('/')[-1]
    local_path = os.path.join(assets_dir, filename)
    
    # Download image
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        
    # Replace URL in HTML with local path
    relative_path = f"assets/sexshop/{filename}"
    html = html.replace(url, relative_path)

with open(sexshop_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated sexshop.html with local image paths.")
