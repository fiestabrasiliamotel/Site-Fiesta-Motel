import os
import re
import urllib.parse

index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"

suites = {
    "Bali": [r"E:\Motel Fiesta\2026\Suíte Bali 02-20260416T175525Z-3-001\Escolhidas para o Site"],
    "Sado": [r"E:\Motel Fiesta\2026\Fotos Sado"],
    "Super Luxo": [r"E:\Motel Fiesta\2026\Suíte Super Luxo Branca 52-20260416T163401Z-3-001\Super Luxo Branca Escolhida para o site"],
    "Luxo": [r"E:\Motel Fiesta\2026\Suíte Luxo-20260416T163326Z-3-001\Escolhidas Site"]
}

def get_encoded_url(d, f):
    path = os.path.join(d, f).replace('\\', '/')
    return "file:///" + urllib.parse.quote(path, safe='/:')

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

for suite_name, dirs in suites.items():
    d = dirs[0]
    if os.path.exists(d):
        files = [f for f in os.listdir(d) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        if files:
            best = files[0]
            for file in files:
                if 'panoramica' in file.lower() or 'horizontal' in file.lower():
                    best = file
                    break
            
            encoded_url = get_encoded_url(d, best)
            
            # Substituição segura que não usa .*? globalmente
            # Procura a tag <img> que precede imediatamente o h3 class="suite-title">Suíte {suite_name}
            # Vamos usar um regex que não cruza tags </div>
            
            pattern = re.compile(rf'(<img alt="Suíte {suite_name}" class="suite-img" src=")([^"]*)("/>)')
            html = pattern.sub(rf'\g<1>{encoded_url}\g<3>', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Imagens da home index.html corrigidas e URL-encoded com sucesso.")
