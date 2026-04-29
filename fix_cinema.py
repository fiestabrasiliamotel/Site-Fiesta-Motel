import os
import re

index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"
suite_path = r"E:\Motel Fiesta\2026\Site novo\suite-cinema.html"

# Correção index.html
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o path quebrado do cinema
bad_src = r"file:///E:/Motel%20Fiesta/2026/Su%C3%ADte%20Cinema%20-%2061-20260323T174027Z-3-001/Melhoradas/Foto%20panoramica%20cama%20cinema%2061.png"
bad_src2 = r"file:///E:/Motel Fiesta/2026/Suíte Cinema - 61-20260323T174027Z-3-001/Escolhodas para site/banheiro suite cinema 61.png"

good_src = r"file:///E:/Motel Fiesta/2026/Suíte Cinema - 61-20260323T174027Z-3-001/Escolhidas para o site/Foto panoramica cama cinema 61 2.png".replace("\\", "/")

# Fallback se houver src antigo
html = re.sub(r'src="[^"]*Cinema[^"]*\.png"', f'src="{good_src}"', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

# Correção suite-cinema.html
with open(suite_path, "r", encoding="utf-8") as f:
    suite_html = f.read()

# Substituir foto hero ruim
suite_html = suite_html.replace(
    'src="file:///E:/Motel Fiesta/2026/Suíte Cinema - 61-20260323T174027Z-3-001/Escolhodas para site/banheiro suite cinema 61.png"',
    f'src="{good_src}"'
)

# Avisar sobre os 2 modelos no texto
old_text = "Suíte temática com foco absoluto em entretenimento e imersão, apresentando 2 ambientes e tela de aproximadamente 150 polegadas."
new_text = "Suíte temática com foco absoluto em entretenimento e imersão. <strong>Atenção: A Suíte Cinema possui duas plantas/modelos diferentes (61 e 33).</strong> Ambas possuem exatamente as mesmas comodidades e padrão de luxo, variando apenas o layout do ambiente."
suite_html = suite_html.replace(old_text, new_text)

# Reescrever a galeria para incluir os dois modelos
dir_61 = r"E:\Motel Fiesta\2026\Suíte Cinema - 61-20260323T174027Z-3-001\Escolhidas para o site"
dir_33 = r"E:\Motel Fiesta\2026\Suíte Cinema 33-20260416T163233Z-3-001\Escolhidas para o site"

def get_images(d):
    images = []
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                path = os.path.join(d, f).replace("\\", "/")
                images.append(f"file:///{path}")
    return images

images_61 = get_images(dir_61)
images_33 = get_images(dir_33)

all_photos = images_61 + images_33
js_array = "[\n" + ",\n".join([f"'{p}'" for p in all_photos]) + "\n]"

# Vamos reconstruir a tag <section class="gallery"> inteira
gallery_html = f"""
    <section class="gallery" id="galeria">
        <div class="section-label reveal">
            <span class="section-label-num">02</span>
            <div class="section-label-line"></div>
            <span class="section-label-text">Galeria</span>
        </div>
        <h2 class="section-title-main reveal">Dois modelos, <em>o mesmo luxo</em></h2>
        <p class="reveal" style="color: var(--gray); font-size: 0.95rem; margin-top: 1rem; margin-bottom: 3rem;">Separamos as fotos por planta para que você possa conferir cada detalhe.</p>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Modelo 61</h3>
        <div class="gallery-grid" style="margin-top: 0; margin-bottom: 5rem;">
"""
# Adicionar 4 fotos do 61
idx = 0
for i in range(min(4, len(images_61))):
    if i == 0:
        gallery_html += f"""
            <div class="gallery-item gallery-item-main" onclick="openLightbox({idx})">
                <img src="{images_61[i]}" alt="Modelo 61">
                <div class="gallery-item-overlay"></div>
            </div>"""
    else:
        gallery_html += f"""
            <div class="gallery-item" onclick="openLightbox({idx})">
                <img src="{images_61[i]}" alt="Modelo 61">
                <div class="gallery-item-overlay"></div>
            </div>"""
    idx += 1

gallery_html += """
        </div>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Modelo 33</h3>
        <div class="gallery-grid" style="margin-top: 0;">
"""

# Adicionar 4 fotos do 33
for i in range(min(4, len(images_33))):
    if i == 0:
        gallery_html += f"""
            <div class="gallery-item gallery-item-main" onclick="openLightbox({idx})">
                <img src="{images_33[i]}" alt="Modelo 33">
                <div class="gallery-item-overlay"></div>
            </div>"""
    else:
        gallery_html += f"""
            <div class="gallery-item" onclick="openLightbox({idx})">
                <img src="{images_33[i]}" alt="Modelo 33">
                <div class="gallery-item-overlay"></div>
            </div>"""
    idx += 1

gallery_html += """
        </div>
    </section>
"""

# Substituir a section.gallery atual
suite_html = re.sub(r'<section class="gallery">.*?</section>', gallery_html, suite_html, flags=re.DOTALL)

# Atualizar o array de fotos JS
suite_html = re.sub(r'const photos = \[.*?\];', f'const photos = {js_array};', suite_html, flags=re.DOTALL)

with open(suite_path, "w", encoding="utf-8") as f:
    f.write(suite_html)

print("Suite Cinema atualizada com sucesso!")
