import os
import re
import urllib.parse

suite_path = r"E:\Motel Fiesta\2026\Site novo\suite-cinema.html"

# Ler o arquivo
with open(suite_path, "r", encoding="utf-8") as f:
    html = f.read()

# Vamos reconstruir o bloco de galeria manualmente e perfeitamente
c61_dir = r"E:\Motel Fiesta\2026\Suíte Cinema - 61-20260323T174027Z-3-001\Escolhidas para o site"
c33_dir = r"E:\Motel Fiesta\2026\Suíte Cinema 33-20260416T163233Z-3-001\Escolhidas para o site"

def get_encoded_url(d, f):
    path = os.path.join(d, f).replace('\\', '/')
    return "file:///" + urllib.parse.quote(path, safe='/:')

# Arquivos a usar
f61 = [
    "Foto panoramica hidro cinema 61 2.png", # Main (projector/bathtub)
    "Foto panoramica cama cinema 61 2.png",  # Small 1
    "Foto panoramica parede cinema 61.png", # Small 2
    "Foto vertical hidro cinema 61 3.png"    # Small 3
]

f33 = [
    "20260402_154442.jpg", # Main
    "20260402_154100.jpg",
    "20260402_154152.jpg",
    "20260402_154334.jpg"
]

# Construir a lista de photos para o JS
all_photos_js = []
for f in f61:
    all_photos_js.append(get_encoded_url(c61_dir, f))
for f in f33:
    all_photos_js.append(get_encoded_url(c33_dir, f))

js_array_str = "[\n" + ",\n".join([f"'{p}'" for p in all_photos_js]) + "\n]"

# HTML da galeria
gallery_html = f"""
    <section class="gallery" id="galeria">
        <div class="section-label reveal">
            <span class="section-label-num">02</span>
            <div class="section-label-line"></div>
            <span class="section-label-text">Galeria</span>
        </div>
        <h2 class="section-title-main reveal">Dois modelos, <em>o mesmo luxo</em></h2>
        <p class="reveal" style="color: var(--gray); font-size: 0.95rem; margin-top: 1rem; margin-bottom: 3rem;">Separamos as fotos por planta para que você possa conferir cada detalhe.</p>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Suíte Cinema 61</h3>
        <div class="gallery-grid" style="margin-top: 0; margin-bottom: 5rem;">

            <div class="gallery-item gallery-item-main" onclick="openLightbox(0)">
                <img src="{get_encoded_url(c61_dir, f61[0])}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(1)">
                <img src="{get_encoded_url(c61_dir, f61[1])}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(2)">
                <img src="{get_encoded_url(c61_dir, f61[2])}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(3)">
                <img src="{get_encoded_url(c61_dir, f61[3])}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Suíte Cinema 33</h3>
        <div class="gallery-grid" style="margin-top: 0;">

            <div class="gallery-item gallery-item-main" onclick="openLightbox(4)">
                <img src="{get_encoded_url(c33_dir, f33[0])}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(5)">
                <img src="{get_encoded_url(c33_dir, f33[1])}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(6)">
                <img src="{get_encoded_url(c33_dir, f33[2])}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(7)">
                <img src="{get_encoded_url(c33_dir, f33[3])}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>
    </section>
"""

# Substituir na section
html = re.sub(r'<section class="gallery" id="galeria">.*?</section>', gallery_html, html, flags=re.DOTALL)

# Substituir no JS
html = re.sub(r'const photos = \[.*?\];', f'const photos = {js_array_str};', html, flags=re.DOTALL)

# Consertar as imagens inline na seção "Sobre a suíte" para usarem URI encodada e apontarem para as fotos certas
html = re.sub(
    r'<div class="reveal" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3px;">.*?</div>\s*</div>\s*</div>',
    f'''<div class="reveal" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3px;">
                <div style="overflow: hidden; height: 260px; grid-column: 1 / 3;">
                    <img src="{get_encoded_url(c61_dir, f61[0])}" alt="Sala da Suíte Cinema" style="width:100%; height:100%; object-fit:cover; transition: transform 0.8s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div style="overflow: hidden; height: 200px;">
                    <img src="{get_encoded_url(c61_dir, f61[1])}" alt="Cama da Suíte Cinema" style="width:100%; height:100%; object-fit:cover; transition: transform 0.8s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div style="overflow: hidden; height: 200px;">
                    <img src="{get_encoded_url(c61_dir, f61[2])}" alt="Detalhe Suíte Cinema" style="width:100%; height:100%; object-fit:cover; transition: transform 0.8s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                </div>
            </div>
        </div>
    </div>''',
    html, flags=re.DOTALL
)

# Consertar Hero image
html = re.sub(r'<div class="hero-bg">\s*<img src=".*?" alt="Suíte Cinema — Fiesta Motel">\s*</div>',
              f'<div class="hero-bg">\n            <img src="{get_encoded_url(c61_dir, f61[0])}" alt="Suíte Cinema — Fiesta Motel">\n        </div>',
              html)


with open(suite_path, "w", encoding="utf-8") as f:
    f.write(html)


# Fix index.html hero card as well
index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

encoded_hero = get_encoded_url(c61_dir, f61[0])
# We need to replace whatever broken URI it has for Cinema
index_html = re.sub(r'src="[^"]*Foto%20panoramica%20hidro%20cinema%2061%202\.png"', f'src="{encoded_hero}"', index_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("All gallery images fixed and URL encoded properly!")
