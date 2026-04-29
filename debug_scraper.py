import urllib.request
import re
import ssl

url = "https://www.fiestamotel.com.br/cardapiofiesta/"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as response:
    html = response.read().decode('utf-8', errors='ignore')

# The original site is built with Elementor or similar. Let's extract heading tags or text near images.
# Actually, let's just dump all text inside h3/h4/h2 and adjacent images.
from html.parser import HTMLParser

class MenuParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
        self.current_tag = ""
        self.last_img = None
        self.last_title = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'img':
            src = dict(attrs).get('src')
            if src:
                self.last_img = src

    def handle_data(self, data):
        text = data.strip()
        if not text: return
        # In Elementor, titles might be in h2, h3, h4 or special spans
        if self.current_tag in ['h1', 'h2', 'h3', 'h4', 'strong'] or len(text) > 4:
            # Simple heuristic to print nearby text and image
            self.items.append((text, self.last_img))

parser = MenuParser()
parser.feed(html)

with open('scraped_dump.txt', 'w', encoding='utf-8') as f:
    for text, img in parser.items:
        if img:
            f.write(f"TEXT: {text}\nIMG: {img}\n\n")

print("Dumped to scraped_dump.txt")
