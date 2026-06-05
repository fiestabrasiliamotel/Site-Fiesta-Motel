import os

site_dir = r"E:\Motel Fiesta\2026\Site novo"
suites = [f for f in os.listdir(site_dir) if f.startswith('suite-') and f.endswith('.html')]

# The navigation menu that should replace the current one
new_nav = """    <!-- NAV -->
    <nav class="nav scrolled" id="nav" style="background: rgba(5,5,5,0.95); padding: 1rem 3rem;">
        <a class="nav-logo" href="index.html">
            FIESTA <span class="title-stroke">MOTEL</span>
        </a>
        <ul class="nav-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="index.html#suites">Suítes</a></li>
            <li><a href="cardapio.html">Cardápio</a></li>
        </ul>
        <a class="nav-cta" href="https://wa.me/556133726060?text=Ol%C3%A1%21%20Gostaria%20de%20fazer%20uma%20reserva." target="_blank">Reservar Agora</a>
    </nav>"""

for suite in suites:
    filepath = os.path.join(site_dir, suite)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Navigation
    nav_start = html.find('<nav id="nav">')
    if nav_start == -1:
        nav_start = html.find('<nav class="nav')
    
    if nav_start != -1:
        nav_end = html.find('</nav>', nav_start) + 6
        html = html[:nav_start] + new_nav + html[nav_end:]

    # 2. Update Gradient Opacity
    # Old gradient: linear-gradient(to right, rgba(5,5,5,0.85) 0%, rgba(5,5,5,0.5) 55%, transparent 100%),
    #               linear-gradient(to top, #050505 0%, rgba(5,5,5,0.6) 35%, transparent 65%)
    # New gradient: less dark so photo shines
    old_grad = """linear-gradient(to right, rgba(5,5,5,0.85) 0%, rgba(5,5,5,0.5) 55%, transparent 100%),
                linear-gradient(to top, #050505 0%, rgba(5,5,5,0.6) 35%, transparent 65%)"""
    new_grad = """linear-gradient(to right, rgba(5,5,5,0.65) 0%, rgba(5,5,5,0.3) 55%, transparent 100%),
                linear-gradient(to top, #050505 0%, rgba(5,5,5,0.3) 35%, transparent 65%)"""
    html = html.replace(old_grad, new_grad)
    
    old_grad2 = """linear-gradient(to right, rgba(5,5,5,0.85) 0%, rgba(5,5,5,0.5) 55%, transparent 100%)"""
    new_grad2 = """linear-gradient(to right, rgba(5,5,5,0.65) 0%, rgba(5,5,5,0.3) 55%, transparent 100%)"""
    html = html.replace(old_grad2, new_grad2)

    # 3. If suite-luxo, change hero image
    if suite == 'suite-luxo.html':
        # Replace the hero image from copa to quarto
        # The current hero img is likely assets/site_images/20260402_171124.jpg (or similar)
        # We need to change the src of <div class="hero-bg"><img src="..."></div>
        # I'll just find the first img in <div class="hero-bg">
        hero_bg_start = html.find('<div class="hero-bg">')
        if hero_bg_start != -1:
            img_start = html.find('<img src="', hero_bg_start)
            img_end = html.find('"', img_start + 10)
            # Find the photo of the quarto in the gallery of suite-luxo.html
            # Let's use 20260402_171104.jpg or similar. We can see it in gallery-item.
            # I will just use assets/site_images/20260402_171104.jpg assuming it's the quarto
            html = html[:img_start+10] + "assets/site_images/20260402_171104.jpg" + html[img_end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Updated suites navigation, gradients, and luxo hero image.")
