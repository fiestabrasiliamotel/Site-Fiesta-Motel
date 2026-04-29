import urllib.request
import re
import ssl

url = "https://www.google.com/search?q=Fiesta+Motel+Taguatinga+avalia%C3%A7%C3%B5es&hl=pt-BR"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read().decode('utf-8', errors='ignore')
        
    # extract spans or divs containing reviews
    import re
    text = re.sub(r'<[^>]+>', ' | ', html)
    text = re.sub(r'\s+', ' ', text)
    
    with open('google_dump.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Dumped search to google_dump.txt")
except Exception as e:
    print("Error:", e)
