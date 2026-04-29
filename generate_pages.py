import os
import re
import glob

# Configurações das suítes
suites = {
    "luxo": {
        "title": "Suíte Luxo",
        "subtitle": "Praticidade, conforto e discrição",
        "description1": "A Suíte Luxo é a porta de entrada para a experiência do Fiesta. Focada em praticidade, conforto e discrição.",
        "description2": "Ideal para quem busca um ambiente funcional com ótimo custo-benefício, sem abrir mão da qualidade e do conforto para momentos especiais.",
        "quote": "A escolha perfeita para um encontro discreto e inesquecível.",
        "price_dom_qua": "R$ 89",
        "price_qui_sab": "R$ 115",
        "directories": [r"E:\Motel Fiesta\2026\Suíte Luxo-20260416T163326Z-3-001\Escolhidas Site"],
        "amenities": [
            ("Cama Redonda", "Cama redonda confortável para seu descanso.", "solar:bed-bold"),
            ("Smart TV", "Canais eróticos e musicais.", "solar:tv-bold"),
            ("Ar-condicionado", "Climatização ideal.", "solar:wind-bold"),
            ("Frigobar", "Bebidas na temperatura certa.", "solar:fridge-bold"),
            ("Sistema de Som", "Som FM para criar o clima.", "solar:boombox-bold"),
            ("Iluminação Especial", "Perfeita para fotos e vídeos.", "solar:lightbulb-bold"),
            ("Garagem Privativa", "Total discrição garantida.", "mdi:car")
        ]
    },
    "fiesta": {
        "title": "Suíte Fiesta",
        "subtitle": "Ambiente totalmente reformado e moderno",
        "description1": "Versão evoluída da Luxo, a Suíte Fiesta apresenta um ambiente totalmente reformado e mais moderno.",
        "description2": "Mais sofisticada, com foco em estética e experiência visual. Um projeto luminotécnico moderno com iluminação cenográfica para momentos únicos.",
        "quote": "Design e modernidade para quem valoriza a estética.",
        "price_dom_qua": "R$ 120",
        "price_qui_sab": "R$ 139",
        "directories": [r"E:\Motel Fiesta\2026\Suíte Fiesta 16-20260323T174126Z-3-001\Escolhidas Site"],
        "amenities": [
            ("Cama Redonda", "Cama redonda muito confortável.", "solar:bed-bold"),
            ("Projeto Luminotécnico", "Iluminação moderna e cenográfica.", "solar:lightbulb-bold"),
            ("Smart TV", "Canais eróticos e musicais.", "solar:tv-bold"),
            ("Ar-condicionado", "Climatização perfeita.", "solar:wind-bold"),
            ("Frigobar", "Bebidas sempre geladas.", "solar:fridge-bold"),
            ("Sistema de Som", "Sistema de som imersivo.", "solar:boombox-bold"),
            ("Garagem Privativa", "Entrada discreta e exclusiva.", "mdi:car")
        ]
    },
    "super-luxo": {
        "title": "Suíte Super Luxo",
        "subtitle": "Conforto, relaxamento e personalização",
        "description1": "A primeira categoria com hidromassagem e o início da experiência mais completa.",
        "description2": "Ideal para quem busca mais conforto, relaxamento e personalização. Possui 3 variações de estilos: Branca, Preta e Laranja, onde o diferencial é o acabamento exclusivo de cada uma.",
        "quote": "Sua porta de entrada para um novo nível de relaxamento.",
        "price_dom_qua": "R$ 139",
        "price_qui_sab": "R$ 159",
        "directories": [
            r"E:\Motel Fiesta\2026\Suíte Super Luxo Branca 52-20260416T163401Z-3-001\Super Luxo Branca Escolhida para o site",
            r"E:\Motel Fiesta\2026\Suite Super Luxo laranja 53-20260416T163437Z-3-001\Escolhidas Site",
            r"E:\Motel Fiesta\2026\Super Luxo Preta - 54-20260323T180317Z-3-001\Escolhidas Site"
        ],
        "amenities": [
            ("Cama Confortável", "Para seu máximo descanso.", "solar:bed-bold"),
            ("Hidromassagem", "Hidromassagem moderna para relaxar.", "solar:bath-bold"),
            ("Smart TV", "Entretenimento na sua tela.", "solar:tv-bold"),
            ("Ar-condicionado", "Climatização no ponto ideal.", "solar:wind-bold"),
            ("Frigobar", "Diversas opções de bebidas.", "solar:fridge-bold"),
            ("Som Bluetooth", "Coloque sua própria playlist.", "solar:boombox-bold"),
            ("Iluminação Especial", "Crie a atmosfera perfeita.", "solar:lightbulb-bold"),
            ("Garagem Privativa", "Total segurança e discrição.", "mdi:car")
        ]
    },
    "cinema": {
        "title": "Suíte Cinema",
        "subtitle": "Foco em entretenimento e imersão",
        "description1": "Suíte temática com foco absoluto em entretenimento e imersão, apresentando 2 ambientes e tela de aproximadamente 150 polegadas.",
        "description2": "Experimente o cinema dentro da suíte, com sistema Home Theater, streaming com lançamentos, hidromassagem moderna e muito mais.",
        "quote": "Uma experiência cinematográfica incomparável.",
        "price_dom_qua": "R$ 199",
        "price_qui_sab": "R$ 249",
        "directories": [
            r"E:\Motel Fiesta\2026\Suíte Cinema - 61-20260323T174027Z-3-001\Escolhodas para site",
            r"E:\Motel Fiesta\2026\Suíte Cinema 33-20260416T163233Z-3-001\Suíte Cinema 33"
        ],
        "amenities": [
            ("Tela de 150''", "Tela gigante com Home Theater.", "solar:tv-bold"),
            ("Streaming Lançamentos", "Seus filmes e séries favoritos.", "solar:play-circle-bold"),
            ("2 Ambientes", "Espaço amplo e dividido.", "solar:home-bold"),
            ("Hidromassagem", "Hidromassagem moderna.", "solar:bath-bold"),
            ("2 Ar-condicionados", "Um split por ambiente.", "solar:wind-bold"),
            ("Som Bluetooth", "Conectividade fácil e rápida.", "solar:boombox-bold"),
            ("Sex Shop no Quarto", "Produtos à sua disposição.", "mdi:shopping"),
            ("Garagem Privativa", "Exclusividade na entrada.", "mdi:car")
        ]
    },
    "bali": {
        "title": "Suíte Bali",
        "subtitle": "Proposta sensorial e relaxante",
        "description1": "Suíte ampla com proposta sensorial e relaxante, trazendo um ambiente acolhedor, amplo e intimista.",
        "description2": "Com 2 ambientes climatizados, cama King e hidromassagem, é o refúgio perfeito para fugir da rotina.",
        "quote": "Uma viagem sensorial inesquecível.",
        "price_dom_qua": "R$ 199",
        "price_qui_sab": "R$ 249",
        "directories": [r"E:\Motel Fiesta\2026\Suíte Bali 02-20260416T175525Z-3-001\Escolhidas para o Site"],
        "amenities": [
            ("Cama King", "Muito mais espaço e conforto.", "solar:bed-bold"),
            ("Hidromassagem", "Relaxe com estilo.", "solar:bath-bold"),
            ("2 Ambientes", "Ambiente acolhedor e amplo.", "solar:home-bold"),
            ("2 Ar-condicionados", "Climatização em toda a suíte.", "solar:wind-bold"),
            ("Som Bluetooth", "Sua playlist preferida tocando.", "solar:boombox-bold"),
            ("Smart TV", "Conteúdo online à vontade.", "solar:tv-bold"),
            ("Sex Shop no Quarto", "Produtos variados e discretos.", "mdi:shopping"),
            ("Garagem Privativa", "Sigilo total na sua chegada.", "mdi:car")
        ]
    },
    "sado": {
        "title": "Suíte Sado",
        "subtitle": "Proposta intensa e fora do padrão",
        "description1": "Suíte temática única, com proposta intensa e totalmente fora do padrão convencional. Existe apenas 1 unidade exclusiva.",
        "description2": "Equipada com cama King em estrutura de ferro, hidromassagem para até 4 pessoas, guilhotina, cruz de São Tomé, gaiola e muito mais.",
        "quote": "Experiência extrema e exclusiva, para um público específico.",
        "price_dom_qua": "R$ 199",
        "price_qui_sab": "R$ 249",
        "directories": [r"E:\Motel Fiesta\2026\Fotos Sado"],
        "amenities": [
            ("Cama King de Ferro", "Cama King em estrutura de ferro.", "solar:bed-bold"),
            ("Estrutura Temática", "Guilhotina, Cruz, Gaiola e Cordas.", "mdi:handcuffs"),
            ("Hidro para 4", "Hidromassagem grande.", "solar:bath-bold"),
            ("2 Ambientes", "Muito espaço disponível.", "solar:home-bold"),
            ("2 Ar-condicionados", "Climatização potente.", "solar:wind-bold"),
            ("Som Bluetooth", "Trilha sonora personalizada.", "solar:boombox-bold"),
            ("Smart TV", "Entretenimento sob demanda.", "solar:tv-bold"),
            ("Sex Shop no Quarto", "Para complementar a experiência.", "mdi:shopping")
        ]
    }
}

def get_images(dirs):
    images = []
    for d in dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    # Use absolute file uri
                    path = os.path.join(d, f).replace("\\", "/")
                    images.append(f"file:///{path}")
    return images

# Template path
base_path = r"E:\Motel Fiesta\2026\Site novo\suite-premium.html"
with open(base_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Helpers para substituir HTML
def replace_between(content, start_marker, end_marker, replacement):
    pattern = re.compile(f"({re.escape(start_marker)}).*?({re.escape(end_marker)})", re.DOTALL)
    return pattern.sub(f"\\1\n{replacement}\n\\2", content)

for slug, data in suites.items():
    html = template
    
    # Title tag and meta
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} — Fiesta Motel Brasília</title>', html)
    
    # Breadcrumb e Títulos Hero
    html = re.sub(r'<span style="color: var\(--white\);">Premium</span>', f'<span style="color: var(--white);">{data["title"].replace("Suíte ", "")}</span>', html)
    html = re.sub(r'<h1 class="hero-title">Suíte<br><strong>Premium</strong></h1>', f'<h1 class="hero-title">Suíte<br><strong>{data["title"].replace("Suíte ", "")}</strong></h1>', html)
    html = re.sub(r'<p class="hero-subtitle">Sofisticação em dois ambientes únicos</p>', f'<p class="hero-subtitle">{data["subtitle"]}</p>', html)
    
    # Textos da seção A Experiência
    html = re.sub(r'<p class="reveal" style="color: var\(--gray-light\); font-size: 1.05rem; font-weight: 300; line-height: 1.85; margin-top: 1.8rem;">.*?</p>', f'<p class="reveal" style="color: var(--gray-light); font-size: 1.05rem; font-weight: 300; line-height: 1.85; margin-top: 1.8rem;">{data["description1"]}</p>', html, flags=re.DOTALL)
    html = re.sub(r'<p class="reveal" style="color: var\(--gray-light\); font-size: 1.05rem; font-weight: 300; line-height: 1.85; margin-top: 1.2rem;">.*?</p>', f'<p class="reveal" style="color: var(--gray-light); font-size: 1.05rem; font-weight: 300; line-height: 1.85; margin-top: 1.2rem;">{data["description2"]}</p>', html, flags=re.DOTALL)
    html = re.sub(r'<p class="reveal" style="color: var\(--gray\); font-size: 0.95rem; font-weight: 300; line-height: 1.7; margin-top: 1.2rem; font-style: italic;">.*?</p>', f'<p class="reveal" style="color: var(--gray); font-size: 0.95rem; font-weight: 300; line-height: 1.7; margin-top: 1.2rem; font-style: italic;">&ldquo;{data["quote"]}&rdquo;</p>', html, flags=re.DOTALL)
    
    # Preços Hero e Tabela
    html = re.sub(r'<strong>R\$ 199</strong> / 2h', f'<strong>{data["price_dom_qua"]}</strong> / 2h', html)
    
    html = re.sub(r'<span class="pricing-value"><span>R\$</span> 199</span>', f'<span class="pricing-value"><span>R$</span> {data["price_dom_qua"].replace("R$ ", "")}</span>', html)
    html = re.sub(r'<span class="pricing-value"><span>R\$</span> 249</span>', f'<span class="pricing-value"><span>R$</span> {data["price_qui_sab"].replace("R$ ", "")}</span>', html)
    
    # Nome no Ambient Text
    html = re.sub(r'<div class="ambient-text">PREMIUM</div>', f'<div class="ambient-text">{data["title"].replace("Suíte ", "").upper()}</div>', html)
    
    # Amenities
    amenities_html = ""
    for name, detail, icon in data["amenities"]:
        amenities_html += f"""
            <div class="amenity-item reveal">
                <div class="amenity-icon"><span class="iconify" data-icon="{icon}"></span></div>
                <div class="amenity-name">{name}</div>
                <div class="amenity-detail">{detail}</div>
            </div>"""
    html = replace_between(html, '<div class="amenities-grid" style="grid-template-columns: repeat(4, 1fr);">', '</section>', amenities_html + "\n        </div>\n    ")
    
    # Imagens
    images = get_images(data["directories"])
    if not images:
        images = [""] * 10  # Fallback
        
    # Atualiza as imagens Hero, Experiência e Galeria se houver imagens
    if len(images) > 0:
        hero_img = images[0]
        html = re.sub(r'<div class="hero-bg">\s*<img src=".*?" alt=".*?">\s*</div>', f'<div class="hero-bg">\n            <img src="{hero_img}" alt="{data["title"]} — Fiesta Motel">\n        </div>', html)
        
        # 3 imagens na seção experiência
        img1 = images[min(1, len(images)-1)]
        img2 = images[min(2, len(images)-1)]
        img3 = images[min(3, len(images)-1)]
        
        # Galeria
        gal_img1 = images[min(4, len(images)-1)]
        gal_img2 = images[min(5, len(images)-1)]
        gal_img3 = images[min(6, len(images)-1)]
        gal_img4 = images[min(7, len(images)-1)]
        
        # Encontra todos os src de imagem no documento que começam com file:/// e substitui sequencialmente
        import re
        
        # Primeiro, substitui a imagem do hero
        html = re.sub(r'<div class="hero-bg">\s*<img src="[^"]+" alt="[^"]+">\s*</div>', f'<div class="hero-bg">\n            <img src="{hero_img}" alt="{data["title"]} — Fiesta Motel">\n        </div>', html)
        
        # Agora para as demais (Experiência e Galeria)
        rest_images = [img1, img2, img3, gal_img1, gal_img2, gal_img3, gal_img4]
        
        def replace_src(match):
            if rest_images:
                return f'src="{rest_images.pop(0)}"'
            return match.group(0)
            
        # Substituir os src="..." das tags img subsequentes (após a seção hero que já foi alterada)
        parts = html.split('<div class="divider">', 1)
        if len(parts) == 2:
            hero_part, rest_part = parts
            rest_part = re.sub(r'src="file:///[^"]+"', replace_src, rest_part)
            html = hero_part + '<div class="divider">' + rest_part
            
        # Lightbox JS array
        photos_array = ",\n            ".join([f"'{img}'" for img in images[:15]])
        html = re.sub(r'const photos = \[.*?\];', f'const photos = [\n            {photos_array}\n        ];', html, flags=re.DOTALL)
        
    out_path = fr"E:\Motel Fiesta\2026\Site novo\suite-{slug}.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("HTMLs gerados com sucesso!")
