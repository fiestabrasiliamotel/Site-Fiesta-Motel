import os
import re

suite_path = r"E:\Motel Fiesta\2026\Site novo\suite-cinema.html"

with open(suite_path, "r", encoding="utf-8") as f:
    html = f.read()

# The JS photos array is already correct and contains all files.
# Let's extract the photos array so we know the exact indexes.
match = re.search(r'const photos = \[(.*?)\];', html, re.DOTALL)
if match:
    photos_str = match.group(1)
    photos = [p.strip().strip("'") for p in photos_str.split(',')]
else:
    print("Could not find photos array")
    exit()

def get_index(filename):
    for i, p in enumerate(photos):
        if filename in p:
            return i
    return 0

# Cinema 61 preferred files:
c61_files = [
    "Foto panoramica hidro cinema 61 2.png", # Main
    "Foto panoramica cama cinema 61 2.png",
    "Foto panoramica parede cinema 61.png",
    "Foto vertical hidro cinema 61 3.png"
]

# Cinema 33 preferred files:
c33_files = [
    "20260402_154442.jpg", # Main
    "20260402_154100.jpg",
    "20260402_154152.jpg",
    "20260402_154334.jpg"
]

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

            <div class="gallery-item gallery-item-main" onclick="openLightbox({get_index(c61_files[0])})">
                <img src="{photos[get_index(c61_files[0])]}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox({get_index(c61_files[1])})">
                <img src="{photos[get_index(c61_files[1])]}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox({get_index(c61_files[2])})">
                <img src="{photos[get_index(c61_files[2])]}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox({get_index(c61_files[3])})">
                <img src="{photos[get_index(c61_files[3])]}" alt="Suíte Cinema 61">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>

        <h3 class="reveal" style="color: var(--gold-light); margin-bottom: 1.5rem; font-family: var(--sans); font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Suíte Cinema 33</h3>
        <div class="gallery-grid" style="margin-top: 0;">

            <div class="gallery-item gallery-item-main" onclick="openLightbox({get_index(c33_files[0])})">
                <img src="{photos[get_index(c33_files[0])]}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox({get_index(c33_files[1])})">
                <img src="{photos[get_index(c33_files[1])]}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox({get_index(c33_files[2])})">
                <img src="{photos[get_index(c33_files[2])]}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
            <div class="gallery-item" onclick="openLightbox({get_index(c33_files[3])})">
                <img src="{photos[get_index(c33_files[3])]}" alt="Suíte Cinema 33">
                <div class="gallery-item-overlay"></div>
            </div>
        </div>
    </section>
"""

html = re.sub(r'<section class="gallery" id="galeria">.*?</section>', gallery_html, html, flags=re.DOTALL)

with open(suite_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Gallery html completely rebuilt with correct indexes.")
