import os
import re
from urllib.parse import quote

index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

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

def get_best_image(dirs):
    all_images = []
    for d in dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    all_images.append(os.path.join(d, f))
    
    if not all_images:
        return ""
        
    # Tenta achar panoramica ou horizontal primeiro
    for img in all_images:
        if 'panoramica' in img.lower() or 'horizontal' in img.lower() or 'ampla' in img.lower():
            return img.replace('\\', '/')
            
    # Se não, pega a primeira
    return all_images[0].replace('\\', '/')

for suite_name, dirs in suites.items():
    img_path = get_best_image(dirs)
    if not img_path:
        continue
    
    # Criar a URL válida com espaços codificados ou não (os navegadores lidam bem com espaços se estiver na tag src="" mas para garantir o padrao faremos uri format)
    # Mas em local, file:///E:/caminho/com espaços.jpg funciona. Para evitar quebra, manteremos como está
    file_url = f"file:///{img_path}"
    
    # Encontrar o bloco da suite específica e atualizar seu <img>
    # Procuramos o <h3 class="suite-title">Suíte {suite_name}</h3>
    # E trocamos o src da imagem que vem ANTES dele no mesmo suite-card
    
    pattern = re.compile(rf'(<div class="suite-card.*?>\s*<div class="suite-img-wrapper">\s*<img alt=".*?" class="suite-img" src=")(.*?)("/>\s*</div>\s*<div class="suite-info">\s*<div class="suite-meta">.*?</div>\s*<h3 class="suite-title">Suíte {suite_name}</h3>)', re.DOTALL | re.IGNORECASE)
    
    match = pattern.search(html)
    if match:
        html = html[:match.start(2)] + file_url + html[match.end(2):]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Imagens atualizadas com sucesso!")
