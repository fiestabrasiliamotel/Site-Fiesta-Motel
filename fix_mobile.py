import os
import re
import glob

# 1. Update style.css
with open("style.css", "a", encoding="utf-8") as f:
    f.write("""
/* ========== MOBILE MENU & FIXES ========== */
.mobile-menu-btn { display: none; }
.mobile-menu { display: none; }

@media (max-width: 900px) {
    .nav { padding: 1rem 1.5rem !important; }
    .nav.scrolled { padding: 1rem 1.5rem !important; }
    .nav-links, .nav-cta { display: none !important; }
    
    .mobile-menu-btn {
        display: flex;
        color: var(--white);
        font-size: 2rem;
        cursor: pointer;
        z-index: 1001;
    }
    .mobile-menu {
        position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
        background: rgba(5,5,5,0.98);
        backdrop-filter: blur(10px);
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        gap: 2rem; z-index: 1000;
        transform: translateY(-100%); transition: transform 0.4s var(--ease-out-expo);
    }
    .mobile-menu.active { transform: translateY(0); display: flex; }
    .mobile-menu a { font-size: 1.5rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--white); transition: color 0.3s ease; }
    .mobile-menu a:hover { color: var(--accent-light); }
    
    /* Adjust paddings for mobile */
    .hero-content { padding: 6rem 1.5rem 3rem !important; }
    section, .services, .about-suite { padding: 4rem 1.5rem !important; }
    .suites { padding: 4rem 1.5rem !important; }
    .footer { padding: 3rem 1.5rem 1.5rem !important; }
    .experiencias { padding: 4rem 1.5rem !important; }
    .amenities-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 1rem !important; }
    .gallery-grid { grid-template-columns: 1fr !important; grid-template-rows: auto !important; }
    .pricing-grid { grid-template-columns: 1fr !important; }
    .hero-title { font-size: clamp(2.2rem, 8vw, 3.5rem) !important; }
    .about-suite > div { grid-template-columns: 1fr !important; gap: 3rem !important; }
    .suite-card { min-width: 85vw !important; width: 85vw !important; }
    .gastronomia-inner { padding: 4rem 1.5rem !important; }
    .gastro-mosaic { grid-template-columns: 1fr !important; grid-template-rows: auto !important; }
}
""")

print("Appended mobile CSS to style.css")

html_files = glob.glob("*.html")

menu_html = """
    <!-- MOBILE MENU -->
    <div class="mobile-menu" id="mobileMenu">
        <a href="index.html" onclick="toggleMobileMenu()">Home</a>
        <a href="index.html#suites" onclick="toggleMobileMenu()">Suítes</a>
        <a href="cardapio.html" onclick="toggleMobileMenu()">Cardápio</a>
        <a href="https://wa.me/556133726060?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." style="margin-top:2rem; font-size:1rem; padding: 1rem 2rem; border: 1px solid var(--accent); color: var(--accent-light);" target="_blank" onclick="toggleMobileMenu()">Reservar Agora</a>
    </div>
"""

script_html = """
    <script>
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            if(menu) menu.classList.toggle('active');
        }
    </script>
</body>
"""

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # If already has mobileMenu, skip
    if 'id="mobileMenu"' in content:
        continue

    # Add mobile-menu-btn to nav
    # Find </nav> and insert the btn right before it
    btn_html = ' <div class="mobile-menu-btn" onclick="toggleMobileMenu()"><span class="iconify" data-icon="solar:hamburger-menu-linear"></span></div>\n    </nav>'
    content = re.sub(r'</nav>', btn_html, content)

    # Insert the mobile menu right after </nav>
    content = re.sub(r'(</nav>)', r'\1\n' + menu_html, content)

    # Insert the script right before </body>
    content = content.replace("</body>", script_html)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Processed {file}")

print("Mobile fixes applied successfully.")
