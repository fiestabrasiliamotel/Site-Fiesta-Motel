import os
import re

site_dir = r"E:\Motel Fiesta\2026\Site novo"

new_nav_links = """        <ul class="nav-links">
            <li><a href="index.html#home">Home</a></li>
            <li><a href="index.html#suites">Suítes</a></li>
            <li><a href="index.html#promocoes">Promoções</a></li>
            <li><a href="cardapio.html">Cardápio</a></li>
            <li><a href="sexshop.html">Sex Shop</a></li>
            <li><a href="index.html#localizacao">Como Chegar</a></li>
        </ul>"""

new_mobile_menu = """    <div class="mobile-menu" id="mobileMenu">
        <a href="index.html#home" onclick="toggleMobileMenu()">Home</a>
        <a href="index.html#suites" onclick="toggleMobileMenu()">Suítes</a>
        <a href="index.html#promocoes" onclick="toggleMobileMenu()">Promoções</a>
        <a href="cardapio.html" onclick="toggleMobileMenu()">Cardápio</a>
        <a href="sexshop.html" onclick="toggleMobileMenu()">Sex Shop</a>
        <a href="index.html#localizacao" onclick="toggleMobileMenu()">Como Chegar</a>
        <a href="https://wa.me/5561992827596?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." style="margin-top:2rem; font-size:1rem; padding: 1rem 2rem; border: 1px solid var(--accent); color: var(--accent-light);" target="_blank" onclick="toggleMobileMenu()">Reservar Agora</a>
    </div>"""

def update_menus():
    html_files = [f for f in os.listdir(site_dir) if f.endswith('.html')]
    
    for filename in html_files:
        filepath = os.path.join(site_dir, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        print(f"Atualizando menus de {filename}...")
        
        # Substitui o bloco <ul class="nav-links">...</ul>
        content = re.sub(r'<ul class="nav-links">.*?</ul>', new_nav_links, content, flags=re.DOTALL)
        
        # Substitui o bloco <div class="mobile-menu" id="mobileMenu">...</div>
        content = re.sub(r'<div class="mobile-menu" id="mobileMenu">.*?</div>', new_mobile_menu, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Navegação atualizada em todos os arquivos HTML!")

if __name__ == "__main__":
    update_menus()
