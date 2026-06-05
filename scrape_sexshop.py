import os
import re
import cloudscraper
import urllib.parse

url = "https://www.fiestamotel.com.br/sex-shop/"
site_dir = r"E:\Motel Fiesta\2026\Site novo"
html_path = os.path.join(site_dir, "sexshop.html")
assets_dir = os.path.join(site_dir, "assets", "sexshop")

os.makedirs(assets_dir, exist_ok=True)

scraper = cloudscraper.create_scraper()
print(f"Fetching HTML from {url} ...")
response = scraper.get(url)
if response.status_code != 200:
    print(f"Failed to fetch {url}, status code: {response.status_code}")
    exit(1)

remote_html = response.text

# Find all images
img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', remote_html, re.IGNORECASE)
print(f"Found {len(img_matches)} image tags in the remote HTML.")

def clean_url(src):
    if src.startswith('//'): return 'https:' + src
    if src.startswith('/'): return 'https://www.fiestamotel.com.br' + src
    if not src.startswith('http'): return 'https://www.fiestamotel.com.br/sex-shop/' + src
    return src

with open(html_path, "r", encoding="utf-8") as f:
    local_html = f.read()

# Pattern to find the generated products in sexshop.html
# Example:
# <h3 class="food-title" style="margin-bottom: 0.5rem; font-size: 1.2rem;">Bracelete</h3>
card_pattern = re.compile(r'(<div style="height: 250px; overflow: hidden; width: 100%; position: relative;">\s*<img src=")([^"]+)(" alt=")([^"]+)(".*?</style>\s*</div>\s*<div style="padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1;">\s*<h3 class="food-title" style="margin-bottom: 0.5rem; font-size: 1.2rem;">)(.*?)(</h3>)', re.DOTALL)

# wait, the style on my generated images is a bit different, let's just find the card completely:
# We know the product titles. We can just regex for the h3 title, and replace the preceding <img src="...">
# Let's do a more robust regex that finds the src attribute of the img tag that precedes the h3 title.
blocks = re.split(r'(<div class="food-card reveal".*?</div>\s*</div>\s*</div>)', local_html, flags=re.DOTALL)

new_html = ""
# We will iterate through local_html blocks, if it's a food-card, process it.

# We will just parse the local HTML with regex.
# Let's find all product names and their current image src
product_cards = re.findall(r'(<div class="food-card reveal".*?<img src=")([^"]+)(" alt=")([^"]+)(".*?<h3 class="food-title"[^>]*>)(.*?)(</h3>.*?</div>\s*</div>\s*</div>)', local_html, re.DOTALL)

for prefix, old_src, alt_attr, alt_val, middle, title, suffix in product_cards:
    clean_title = title.strip().lower()
    
    # Try to find an image url in remote_html that is close to the text of 'clean_title'
    best_img = None
    pos = remote_html.lower().find(clean_title)
    if pos != -1:
        # Search for the closest image before the title
        prev_img = remote_html.rfind('<img ', 0, pos)
        if prev_img != -1:
            match = re.search(r'src=["\']([^"\']+)["\']', remote_html[prev_img:pos])
            if match:
                best_img = clean_url(match.group(1))
    
    if best_img:
        filename = best_img.split('/')[-1]
        if '?' in filename: filename = filename.split('?')[0]
        local_filepath = os.path.join(assets_dir, filename)
        
        if not os.path.exists(local_filepath):
            print(f"Downloading: {best_img}")
            try:
                img_resp = scraper.get(best_img)
                if img_resp.status_code == 200:
                    with open(local_filepath, 'wb') as out:
                        out.write(img_resp.content)
                else:
                    print(f"Error downloading {best_img}: {img_resp.status_code}")
            except Exception as e:
                print(f"Error downloading {best_img}: {e}")
                
        rel_path = f"assets/sexshop/{filename}"
        
        # Replace old_src with rel_path
        local_html = local_html.replace(prefix + old_src + alt_attr + alt_val + middle + title + suffix, 
                                        prefix + rel_path + alt_attr + alt_val + middle + title + suffix)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(local_html)

print("Sex shop photos updated successfully!")
