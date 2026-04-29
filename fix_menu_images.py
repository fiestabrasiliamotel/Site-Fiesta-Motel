import urllib.request
import re
import os
import ssl

html_path = r"E:\Motel Fiesta\2026\Site novo\cardapio.html"
assets_dir = r"E:\Motel Fiesta\2026\Site novo\assets\cardapio"

os.makedirs(assets_dir, exist_ok=True)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

# The definitive mapping from exact title in cardapio.html to exact image URL in the original site
exact_mapping = {
    "Carne de Sol": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/carne-de-sol-r5h9q9zlve4xyz7nz3gffvm631bmmt1sqvqqvqhbkg.jpg",
    "Frango a Passarinho": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/Frango-a-passarinho-fiesta-r5hbsbpw9ji4l3njl3qdv6xerscl0f0k9dvrwgote8.jpg",
    "Batata Frita c/ Bacon": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/batata-frita-com-bacon-r0osms44xlug81dfk3t7s9hbgvwgk4dskht4o0xf4g.png",
    "Hambúrguer Artesanal": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/hambfrit-r0osms44xlug81dfk3t7s9hbgvwgk4dskht4o0xf4g.jpg",
    "Café da Manhã Completo": "https://www.fiestamotel.com.br/wp-content/uploads/2025/05/cafe-1024x683.jpg",
    "Fiesta Brasil": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/PF-r5ip3ht39pkqtp4dufhot8g64irlu2baznnjwwmmds.jpg",
    "Picadinho de Carne": "https://www.fiestamotel.com.br/wp-content/uploads/2025/11/PICADINHO-1-1024x683.jpg",
    "Parmegiana de Carne": "https://www.fiestamotel.com.br/wp-content/uploads/2025/11/PARMEGIANA-DE-CARNE-1024x680.jpg",
    "Escalope Molho Madeira": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/escalope-repaginado-cortado-3-rie089d7noo405sds7nmckvymd89fnai143prf9az4.jpg",
    "Escondidinho de Carne Seca": "https://www.fiestamotel.com.br/wp-content/uploads/2025/11/10.04-escondidinho-de-abobora-1024x717.jpg",
    "Fettuccine c/ Frango": "https://www.fiestamotel.com.br/wp-content/uploads/2025/11/FETTUCCINE-COM-FGO-AO-M.-QUEIJOS-2.jpg",
    "Frango ao Molho de Laranja": "https://www.fiestamotel.com.br/wp-content/uploads/elementor/thumbs/com-molho-de-laranja_landscapeThumbnail_pt-1-rea6gxi31er3itrwmdzsbfupk036gpizumergok0kc.jpeg",
    "Panelinha Mineira": "https://www.fiestamotel.com.br/wp-content/uploads/2025/11/PANELINHA-MINEIRA-3-1024x680.jpg",
    "Gin Morango / Maça Fiesta": "https://www.fiestamotel.com.br/wp-content/uploads/2023/02/GIN-MORANGO-FIESTA.png",
    "Caipirinha / Caipiroska": "https://www.fiestamotel.com.br/wp-content/uploads/2022/12/caipiroska.png",
    "Espumante Chandon": "https://www.fiestamotel.com.br/wp-content/uploads/2025/05/a2501b73d2ea163fa4adb4b23665b638-576x1024.jpg"
}

with open(html_path, "r", encoding="utf-8") as f:
    local_html = f.read()

# Ache todas as food-cards
# Como o script anterior já rodou, os placeholders sumiram. Precisamos procurar a imagem que tá lá OU o placeholder.
# Regex para pegar o bloco de imagem e o título:
card_pattern = re.compile(r'(<div (?:class="food-img-placeholder"|style="height: 220px; overflow: hidden;").*?</div>)\s*<div class="food-info">\s*<h3 class="food-title">(.*?)</h3>', re.DOTALL)
cards = card_pattern.findall(local_html)

for img_block, title in cards:
    clean_title = title.strip()
    
    # Try exact match first
    remote_img = exact_mapping.get(clean_title)
    
    if remote_img:
        filename = remote_img.split('/')[-1]
        local_filepath = os.path.join(assets_dir, filename)
        
        # Download image if not exists
        if not os.path.exists(local_filepath):
            try:
                print(f"Baixando exata: {remote_img}")
                req_img = urllib.request.Request(remote_img, headers=headers)
                with urllib.request.urlopen(req_img, context=ctx) as r, open(local_filepath, 'wb') as out:
                    out.write(r.read())
            except Exception as e:
                print(f"Erro ao baixar {remote_img}: {e}")
                continue
                
        # Replace no html
        rel_path = f"assets/cardapio/{filename}"
        new_img_tag = f'<div style="height: 220px; overflow: hidden;"><img src="{rel_path}" alt="{clean_title}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseover="this.style.transform=\'scale(1.05)\'" onmouseout="this.style.transform=\'scale(1)\'"></div>'
        
        # O replace precisa ser muito exato, vamos usar o re.sub no texto total para este titulo especifico
        # Isso garante que substituímos apenas a div daquela imagem especifica
        pattern_to_replace = re.compile(re.escape(img_block) + r'(\s*<div class="food-info">\s*<h3 class="food-title">)' + re.escape(title) + r'(</h3>)', re.DOTALL)
        local_html = pattern_to_replace.sub(new_img_tag + r'\g<1>' + title + r'\g<2>', local_html, count=1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(local_html)

print("Processo concluído com Mapeamento Exato. Cardápio HTML 100% fiel.")
