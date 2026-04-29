import os
import re

suite_path = r"E:\Motel Fiesta\2026\Site novo\suite-cinema.html"
index_path = r"E:\Motel Fiesta\2026\Site novo\index.html"

# 1. Update index.html hero image
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = index_html.replace(
    'Foto panoramica cama cinema 61 2.png',
    'Foto panoramica hidro cinema 61 2.png'
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# 2. Update suite-cinema.html
with open(suite_path, "r", encoding="utf-8") as f:
    suite_html = f.read()

# Fix text naming
suite_html = suite_html.replace('plantas/modelos diferentes (61 e 33)', 'opções de plantas diferentes (61 e 33)')
suite_html = suite_html.replace('Modelo 61', 'Suíte Cinema 61')
suite_html = suite_html.replace('Modelo 33', 'Suíte Cinema 33')

# Fix hero image and inline images
suite_html = suite_html.replace(
    'Foto panoramica cama cinema 61 2.png',
    'Foto panoramica hidro cinema 61 2.png'
)

# We want to change the 4 photos for Suite 33 in the gallery.
# Currently they are:
# 20260402_153311.jpg
# 20260402_153900.jpg
# 20260402_153933.jpg
# 20260402_153950.jpg
# We will replace them with files from later in the photoshoot.
suite_html = suite_html.replace('20260402_153311.jpg', '20260402_154100.jpg')
suite_html = suite_html.replace('20260402_153900.jpg', '20260402_154152.jpg')
suite_html = suite_html.replace('20260402_153933.jpg', '20260402_154334.jpg')
suite_html = suite_html.replace('20260402_153950.jpg', '20260402_154442.jpg')

with open(suite_path, "w", encoding="utf-8") as f:
    f.write(suite_html)

print("Images and texts updated successfully!")
