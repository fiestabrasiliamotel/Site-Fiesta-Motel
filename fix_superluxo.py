import os
import re
import urllib.parse

suite_path = r"E:\Motel Fiesta\2026\Site novo\suite-super-luxo.html"
index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"

preta_dir = r"E:\Motel Fiesta\2026\Super Luxo Preta - 54-20260323T180317Z-3-001\Escolhidas Site"
branca_dir = r"E:\Motel Fiesta\2026\Suíte Super Luxo Branca 52-20260416T163401Z-3-001\Super Luxo Branca Escolhida para o site"
laranja_dir = r"E:\Motel Fiesta\2026\Suite Super Luxo laranja 53-20260416T163437Z-3-001\Escolhidas Site"

def get_encoded_url(d, f):
    path = os.path.join(d, f).replace('\\', '/')
    return "file:///" + urllib.parse.quote(path, safe='/:')

# Select the photos for each model
p_preta = ["20260319_162640.jpg", "20260319_162922.jpg", "20260319_162704.jpg", "20260319_162600.jpg"]
p_branca = ["20260402_160802.jpg", "20260402_161747.jpg", "20260402_160637.jpg", "20260402_161806.jpg"]
p_laranja = ["20260402_163634.jpg", "20260402_163722.jpg", "20260402_163504.jpg", "20260402_163839.jpg"]

# Build the JS array with all photos
all_photos = []
all_photos.extend([get_encoded_url(preta_dir, f) for f in p_preta])
all_photos.extend([get_encoded_url(branca_dir, f) for f in p_branca])
all_photos.extend([get_encoded_url(laranja_dir, f) for f in p_laranja])

js_array_str = "[\n" + ",\n".join([f"'{p}'" for p in all_photos]) + "\n]"

gallery_html = f"""
    <section class="gallery">
        <div class="section-label reveal">
            <span class="section-label-num">02</span>
            <div class="section-label-line"></div>
            <span class="section-label-text">Galeria</span>
        </div>
        <h2 class="section-title-main reveal">Três estilos, <em>o mesmo conforto</em></h2>
        <p class="reveal" style="color: var(--gray); font-size: 0.95rem; margin-top: 1rem; margin-bottom: 3rem;">Separamos as fotos por estilo para que você possa escolher a sua preferida.</p>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Suíte Super Luxo Preta (54)</h3>
        <div class="gallery-grid" style="margin-top: 0; margin-bottom: 5rem;">
            <div class="gallery-item gallery-item-main" onclick="openLightbox(0)">
                <img src="{get_encoded_url(preta_dir, p_preta[0])}" alt="Suíte Super Luxo Preta">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(1)">
                <img src="{get_encoded_url(preta_dir, p_preta[1])}" alt="Suíte Super Luxo Preta">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(2)">
                <img src="{get_encoded_url(preta_dir, p_preta[2])}" alt="Suíte Super Luxo Preta">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(3)">
                <img src="{get_encoded_url(preta_dir, p_preta[3])}" alt="Suíte Super Luxo Preta">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Suíte Super Luxo Branca (52)</h3>
        <div class="gallery-grid" style="margin-top: 0; margin-bottom: 5rem;">
            <div class="gallery-item gallery-item-main" onclick="openLightbox(4)">
                <img src="{get_encoded_url(branca_dir, p_branca[0])}" alt="Suíte Super Luxo Branca">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(5)">
                <img src="{get_encoded_url(branca_dir, p_branca[1])}" alt="Suíte Super Luxo Branca">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(6)">
                <img src="{get_encoded_url(branca_dir, p_branca[2])}" alt="Suíte Super Luxo Branca">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(7)">
                <img src="{get_encoded_url(branca_dir, p_branca[3])}" alt="Suíte Super Luxo Branca">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Suíte Super Luxo Laranja (53)</h3>
        <div class="gallery-grid" style="margin-top: 0;">
            <div class="gallery-item gallery-item-main" onclick="openLightbox(8)">
                <img src="{get_encoded_url(laranja_dir, p_laranja[0])}" alt="Suíte Super Luxo Laranja">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(9)">
                <img src="{get_encoded_url(laranja_dir, p_laranja[1])}" alt="Suíte Super Luxo Laranja">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(10)">
                <img src="{get_encoded_url(laranja_dir, p_laranja[2])}" alt="Suíte Super Luxo Laranja">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox(11)">
                <img src="{get_encoded_url(laranja_dir, p_laranja[3])}" alt="Suíte Super Luxo Laranja">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>
    </section>
"""

with open(suite_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace Gallery
html = re.sub(r'<section class="gallery">.*?</section>', gallery_html, html, flags=re.DOTALL)

# Replace JS array
html = re.sub(r'const photos = \[.*?\];', f'const photos = {js_array_str};', html, flags=re.DOTALL)

# Replace Hero Image
html = re.sub(r'<div class="hero-bg">\s*<img src=".*?" alt="Suíte Super Luxo — Fiesta Motel">\s*</div>',
              f'<div class="hero-bg">\n            <img src="{get_encoded_url(preta_dir, p_preta[0])}" alt="Suíte Super Luxo — Fiesta Motel">\n        </div>',
              html)

# Replace text in "A Experiência" to explicitly inform about the 3 versions
old_text = "Ideal para quem busca mais conforto, relaxamento e personalização. Possui 3 variações de estilos: Branca, Preta e Laranja, onde o diferencial é o acabamento exclusivo de cada uma."
new_text = "<strong>Atenção: A Suíte Super Luxo possui 3 opções de estilos de acabamento diferentes (Preta, Branca e Laranja).</strong> Ambas possuem exatamente as mesmas comodidades, hidromassagem e padrão de luxo, variando apenas o design visual do ambiente para você escolher a sua vibe preferida."
html = html.replace(old_text, new_text)

# Replace the 3 inline images in "A Experiência"
html = re.sub(
    r'<div class="reveal" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3px;">.*?</div>\s*</div>\s*</div>',
    f'''<div class="reveal" style="display: grid; grid-template-columns: 1fr 1fr; gap: 3px;">
                <div style="overflow: hidden; height: 260px; grid-column: 1 / 3;">
                    <img src="{get_encoded_url(preta_dir, p_preta[0])}" alt="Suíte Super Luxo Preta" style="width:100%; height:100%; object-fit:cover; transition: transform 0.8s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div style="overflow: hidden; height: 200px;">
                    <img src="{get_encoded_url(preta_dir, p_preta[1])}" alt="Suíte Super Luxo Preta" style="width:100%; height:100%; object-fit:cover; transition: transform 0.8s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div style="overflow: hidden; height: 200px;">
                    <img src="{get_encoded_url(preta_dir, p_preta[2])}" alt="Suíte Super Luxo Preta" style="width:100%; height:100%; object-fit:cover; transition: transform 0.8s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                </div>
            </div>
        </div>
    </div>''',
    html, flags=re.DOTALL
)

with open(suite_path, "w", encoding="utf-8") as f:
    f.write(html)

# Update index.html specifically for Super Luxo
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

pattern = re.compile(rf'(<img alt="Suíte Super Luxo" class="suite-img" src=")([^"]*)("/>)')
index_html = pattern.sub(rf'\g<1>{get_encoded_url(preta_dir, p_preta[0])}\g<3>', index_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Super Luxo page perfectly rebuilt and integrated.")
