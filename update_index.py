import os
import re

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

def get_images(dirs, count=3):
    images = []
    for d in dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    path = os.path.join(d, f).replace("\\", "/")
                    images.append(f"file:///{path}")
                    if len(images) >= count:
                        return images
    return images

index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Adicionar CSS do carrossel no head
carousel_css = """
    <style>
        /* Carrossel nativo nas suites-cards */
        .suite-img-carousel-container {
            position: relative;
            width: 100%;
            height: 100%;
        }
        .suite-img-carousel {
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scrollbar-width: none;
            -ms-overflow-style: none;
            height: 100%;
            width: 100%;
            scroll-behavior: smooth;
        }
        .suite-img-carousel::-webkit-scrollbar { display: none; }
        .suite-img-carousel img {
            flex: 0 0 100%;
            scroll-snap-align: start;
            object-fit: cover;
            width: 100%;
            height: 100%;
        }
        .carousel-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(5,5,5,0.6);
            border: 1px solid rgba(255,255,255,0.1);
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 10;
            transition: all 0.3s;
            opacity: 0;
        }
        .suite-img-carousel-container:hover .carousel-btn {
            opacity: 1;
        }
        .carousel-btn:hover {
            background: rgba(157, 78, 221, 0.8);
        }
        .carousel-prev { left: 10px; }
        .carousel-next { right: 10px; }
        .carousel-dots {
            position: absolute;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 6px;
            z-index: 10;
        }
        .carousel-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            transition: all 0.3s;
        }
        .carousel-dot.active {
            background: var(--accent-light);
            transform: scale(1.3);
        }
    </style>
"""

if "suite-img-carousel" not in html:
    html = html.replace("</head>", carousel_css + "\n</head>")

# Substituir o wrapper
for suite_name, dirs in suites.items():
    images = get_images(dirs, count=4)
    if not images:
        continue
        
    imgs_html = ""
    for idx, img in enumerate(images):
        imgs_html += f'                <img alt="Suíte {suite_name}" src="{img}"/>\n'
        
    carousel_html = f"""<div class="suite-img-wrapper suite-img-carousel-container">
                        <button class="carousel-btn carousel-prev" onclick="scrollCarousel(this, -1)"><span class="iconify" data-icon="solar:alt-arrow-left-linear"></span></button>
                        <div class="suite-img-carousel" onscroll="updateDots(this)">
            {imgs_html}            </div>
                        <button class="carousel-btn carousel-next" onclick="scrollCarousel(this, 1)"><span class="iconify" data-icon="solar:alt-arrow-right-linear"></span></button>
                        <div class="carousel-dots">
                            {"".join(['<div class="carousel-dot' + (' active' if i==0 else '') + '"></div>' for i in range(len(images))])}
                        </div>
                    </div>"""
                    
    # Regex para encontrar a tag <div class="suite-img-wrapper"> correspondente a essa suite
    # Procuramos o bloco todo de card e verificamos pelo h3 class="suite-title" Suíte Name
    
    # É mais fácil buscar a seção específica do card
    pattern = re.compile(rf'<div class="suite-img-wrapper">.*?</div>\s*<div class="suite-info">\s*<div class="suite-meta">[^<]+</div>\s*<h3 class="suite-title">Suíte {suite_name}</h3>', re.DOTALL)
    
    match = pattern.search(html)
    if match:
        old_part = match.group(0)
        new_part = re.sub(r'<div class="suite-img-wrapper">.*?</div>', carousel_html, old_part, flags=re.DOTALL)
        html = html.replace(old_part, new_part)

# Adicionar JS script
js_code = """
        function scrollCarousel(btn, dir) {
            const container = btn.parentElement.querySelector('.suite-img-carousel');
            const width = container.clientWidth;
            container.scrollBy({ left: dir * width, behavior: 'smooth' });
        }
        function updateDots(container) {
            const index = Math.round(container.scrollLeft / container.clientWidth);
            const dots = container.parentElement.querySelectorAll('.carousel-dot');
            dots.forEach((dot, i) => {
                if (i === index) dot.classList.add('active');
                else dot.classList.remove('active');
            });
        }
"""
if "scrollCarousel" not in html:
    html = html.replace("</script>\n</body>", js_code + "\n    </script>\n</body>")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Index.html atualizado com carrosséis e fotos!")
