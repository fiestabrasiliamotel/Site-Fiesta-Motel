import urllib.request
import re
import os
import ssl

url = "https://www.fiestamotel.com.br/cardapiofiesta/"
html_path = r"E:\Motel Fiesta\2026\Site novo\cardapio.html"
assets_dir = r"E:\Motel Fiesta\2026\Site novo\assets\cardapio"

os.makedirs(assets_dir, exist_ok=True)

print(f"Buscando HTML de {url} ...")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        remote_html = response.read().decode('utf-8', errors='ignore')
except Exception as e:
    print(f"Erro ao acessar {url}: {e}")
    exit(1)

# A página original do Fiesta usa algo como <img src="..."> perto do nome do prato.
# Vamos buscar todas as imagens e os nomes em volta.
# Como não sabemos exatamente a estrutura, vamos fazer um regex para achar imgs.
img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', remote_html, re.IGNORECASE)

print(f"Foram encontradas {len(img_matches)} tags de imagem no site original.")

# Baixar as imagens e tentar cruzar os nomes com os títulos no nosso HTML local
def clean_url(src):
    if src.startswith('//'): return 'https:' + src
    if src.startswith('/'): return 'https://www.fiestamotel.com.br' + src
    if not src.startswith('http'): return 'https://www.fiestamotel.com.br/cardapiofiesta/' + src
    return src

# Open local HTML
with open(html_path, "r", encoding="utf-8") as f:
    local_html = f.read()

# Ache todas as food-cards
card_pattern = re.compile(r'(<div class="food-img-placeholder">.*?</div>)\s*(<div class="food-info">\s*<h3 class="food-title">)(.*?)(</h3>)', re.DOTALL)
cards = card_pattern.findall(local_html)

for placeholder, before_title, title, after_title in cards:
    clean_title = title.strip().lower()
    
    # Try to find an image url in remote_html that is close to the text of 'clean_title'
    # Procurar a string de title no HTML original, e pegar a <img src="..."> mais próxima antes ou depois
    title_regex = re.escape(title.strip())
    # Procurar um bloco: <img src="X"> ... Title ... OU ... Title ... <img src="X">
    # Uma forma mais simples: tentar pegar o src de imagem em que o nome do arquivo tenha parte do titulo
    best_img = None
    
    # Heurística 1: Nome do arquivo bate com o título
    words = [w for w in clean_title.split() if len(w) > 3]
    for src in img_matches:
        if any(w in src.lower() for w in words):
            best_img = clean_url(src)
            break
    
    # Heurística 2: Pegar o remote_html, achar a posição do titulo, e achar a tag img mais próxima
    if not best_img:
        pos = remote_html.lower().find(clean_title)
        if pos != -1:
            # Buscar img antes
            prev_img = remote_html.rfind('<img ', 0, pos)
            if prev_img != -1:
                match = re.search(r'src=["\']([^"\']+)["\']', remote_html[prev_img:pos])
                if match: best_img = clean_url(match.group(1))

    if best_img:
        filename = best_img.split('/')[-1]
        if '?' in filename: filename = filename.split('?')[0]
        local_filepath = os.path.join(assets_dir, filename)
        
        # Download image
        if not os.path.exists(local_filepath):
            try:
                print(f"Baixando: {best_img}")
                req_img = urllib.request.Request(best_img, headers=headers)
                with urllib.request.urlopen(req_img, context=ctx) as r, open(local_filepath, 'wb') as out:
                    out.write(r.read())
            except Exception as e:
                print(f"Erro ao baixar {best_img}: {e}")
                continue
                
        # Replace no html
        rel_path = f"assets/cardapio/{filename}"
        new_img_tag = f'<div style="height: 220px; overflow: hidden;"><img src="{rel_path}" alt="{title.strip()}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseover="this.style.transform=\'scale(1.05)\'" onmouseout="this.style.transform=\'scale(1)\'"></div>'
        
        # Substituir no arquivo
        local_html = local_html.replace(placeholder, new_img_tag, 1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(local_html)

print("Processo concluído. Cardápio HTML atualizado.")
