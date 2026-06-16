import os
import re
import urllib.parse

site_dir = r"E:\Motel Fiesta\2026\Site novo"
correct_wpp = "5561992827596"

suite_names = {
    "suite-cinema.html": "Suíte Cinema",
    "suite-premium.html": "Suíte Premium",
    "suite-bali.html": "Suíte Bali",
    "suite-sado.html": "Suíte Sado",
    "suite-luxo.html": "Suíte Luxo",
    "suite-fiesta.html": "Suíte Fiesta",
    "suite-super-luxo.html": "Suíte Super Luxo"
}

def update_html_files():
    html_files = [f for f in os.listdir(site_dir) if f.endswith('.html')]
    
    for filename in html_files:
        filepath = os.path.join(site_dir, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        print(f"Processando {filename}...")
        
        # 1. Substituir todos os números de WhatsApp (33726060 -> 992827596)
        content = content.replace("556133726060", correct_wpp)
        content = content.replace("55613372-6060", correct_wpp)
        
        # 2. Corrigir links de WhatsApp contextualmente
        if filename in suite_names:
            suite_name = suite_names[filename]
            # O link de reserva da suíte deve dizer "Olá! Gostaria de reservar a Suíte X"
            # O link pode estar url-encodado ou semi-encodado
            # Procuramos links wa.me/5561992827596?text=...
            # Substituímos todas as ocorrências de links wa.me para reserva de suíte
            msg_reserva = urllib.parse.quote(f"Olá! Gostaria de reservar a {suite_name}")
            
            # Regex para achar links do WhatsApp na página da suíte
            # Substitui links que tenham ?text=... por ?text=msg_reserva
            # exceto se for o rodapé/menu geral que tem "Olá! Gostaria de fazer uma reserva."
            
            def replace_wpp_suite(match):
                url = match.group(0)
                # Se no texto original existia "fazer uma reserva" ou similar, mantém a mensagem geral
                if "fazer%20uma%20reserva" in url or "fazer uma reserva" in url:
                    msg_geral = urllib.parse.quote("Olá! Gostaria de fazer uma reserva.")
                    return f"https://wa.me/{correct_wpp}?text={msg_geral}"
                # Caso contrário, coloca a mensagem específica da suíte
                return f"https://wa.me/{correct_wpp}?text={msg_reserva}"
            
            content = re.sub(r'https://wa\.me/' + correct_wpp + r'\?text=[^"\']+', replace_wpp_suite, content)
            content = re.sub(r'https://wa\.me/556133726060\?text=[^"\']+', replace_wpp_suite, content) # just in case
            
        elif filename == "cardapio.html":
            # Cardápio deve ter os links dos botões "Pedir" com:
            # "Olá! Estou na suíte e gostaria de pedir o item do cardápio: [Nome do Item]"
            # Já estão assim no cardapio.html, mas vamos garantir o número correto do wpp neles:
            content = content.replace("wa.me/556133726060", f"wa.me/{correct_wpp}")
            
        elif filename == "sexshop.html":
            # Sex shop deve ter os links dos botões "Pedir" com:
            # "Olá! Estou na suíte e gostaria de pedir o item do Sex Shop: [Nome do Item]"
            content = content.replace("wa.me/556133726060", f"wa.me/{correct_wpp}")
            
        else: # index.html e outras páginas gerais
            # WhatsApp na home
            msg_geral = urllib.parse.quote("Olá! Gostaria de fazer uma reserva.")
            content = re.sub(r'https://wa\.me/' + correct_wpp + r'\?text=[^"\']+', f"https://wa.me/{correct_wpp}?text={msg_geral}", content)
            
        # 3. Mover setas do Lightbox para as laterais (apenas páginas de suítes)
        if filename in suite_names:
            # Encontrar bloco de lightbox original:
            # <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
            #     <button class="lightbox-close" onclick="closeLightboxDirect()">✕</button>
            #     <img class="lightbox-img" id="lightbox-img" src="" alt="">
            #     <div class="lightbox-arrows">
            #         <button class="lightbox-btn" onclick="lightboxNav(-1)"><span class="iconify" data-icon="solar:arrow-left-linear"></span></button>
            #         <button class="lightbox-btn" onclick="lightboxNav(1)"><span class="iconify" data-icon="solar:arrow-right-linear"></span></button>
            #     </div>
            # </div>
            
            # Novo bloco de lightbox com setas laterais
            new_lightbox = f"""    <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
        <button class="lightbox-close" onclick="closeLightboxDirect()">✕</button>
        <button class="lightbox-btn prev" onclick="lightboxNav(-1)" style="position: absolute; left: 2rem; top: 50%; transform: translateY(-50%); z-index: 1010; width: 44px; height: 44px; border: 1px solid rgba(255,255,255,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--gray); background: none; transition: all 0.3s ease;"><span class="iconify" data-icon="solar:arrow-left-linear"></span></button>
        <img class="lightbox-img" id="lightbox-img" src="" alt="">
        <button class="lightbox-btn next" onclick="lightboxNav(1)" style="position: absolute; right: 2rem; top: 50%; transform: translateY(-50%); z-index: 1010; width: 44px; height: 44px; border: 1px solid rgba(255,255,255,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--gray); background: none; transition: all 0.3s ease;"><span class="iconify" data-icon="solar:arrow-right-linear"></span></button>
    </div>"""
            
            # Regex para substituir o bloco do lightbox
            content = re.sub(r'<div class="lightbox" id="lightbox".*?</div>\s*</div>', new_lightbox, content, flags=re.DOTALL)
            
            # Adicionar hover effect nas setas no style tag local de cada suíte
            style_hover = """
        .lightbox-btn:hover { color: var(--white) !important; border-color: rgba(255,255,255,0.3) !important; background: rgba(255,255,255,0.05) !important; }
    </style>"""
            content = content.replace("</style>", style_hover)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Atualizações de WhatsApp e Lightbox completadas com sucesso!")

if __name__ == "__main__":
    update_html_files()
