import re
import urllib.parse

html_path = r"E:\Motel Fiesta\2026\Site novo\cardapio.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Vamos achar os blocos completos de info para extrair o titulo e substituir o botao
# Exemplo de bloco:
# <h3 class="food-title">Carne de Sol</h3>
# <p class="food-desc">...</p>
# <div class="food-price">R$ 49,90 <button class="btn-add">Pedir</button></div>

def replace_button(match):
    title = match.group(1).strip()
    encoded_text = urllib.parse.quote(f"Olá! Estou na suíte e gostaria de pedir o item do cardápio: {title}")
    whatsapp_url = f"https://wa.me/5561992827596?text={encoded_text}"
    
    # Monta a nova tag 'a' mantendo a mesma classe btn-add para manter o CSS
    new_btn = f'<a href="{whatsapp_url}" target="_blank" class="btn-add" style="text-decoration: none; display: inline-block;">Pedir</a>'
    
    return f'<h3 class="food-title">{title}</h3>' + match.group(2) + new_btn + match.group(3)

# O regex pega do h3 até o fechamento da tag button (ou seja, captura o que tem no meio).
pattern = re.compile(r'<h3 class="food-title">(.*?)</h3>(.*?)<button class="btn-add">Pedir</button>(.*?(?:</div>))', re.DOTALL)

new_html = pattern.sub(replace_button, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Botões substituídos por links do WhatsApp.")
