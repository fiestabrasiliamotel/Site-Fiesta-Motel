import os
import re
import shutil
import urllib.parse

def copy_and_update_assets():
    site_dir = r"E:\Motel Fiesta\2026\Site novo"
    assets_dir = os.path.join(site_dir, "assets", "site_images")
    
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        
    html_files = [f for f in os.listdir(site_dir) if f.endswith('.html')]
    
    # regex to find file:///E:... 
    # it can be in src="file:///..." or url('file:///...')
    # we need to be careful with quotes and spaces.
    pattern = re.compile(r'file:///E:/[A-Za-z0-9_\-\.%/]+', re.IGNORECASE)
    
    for filename in html_files:
        filepath = os.path.join(site_dir, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        matches = pattern.findall(content)
        if not matches:
            continue
            
        print(f"Processing {filename} - Found {len(matches)} absolute paths")
        new_content = content
        for match in set(matches):
            # decode URL
            local_path = urllib.parse.unquote(match.replace("file:///", ""))
            # Ensure it uses backslashes for windows
            local_path = local_path.replace('/', '\\')
            
            if os.path.exists(local_path):
                # Copy file
                basename = os.path.basename(local_path)
                # handle name collisions if needed, but assuming unique names for now
                # to be safe, prepend part of the folder name or just use basename
                safe_name = basename.replace(' ', '_').replace('%20', '_')
                dest_path = os.path.join(assets_dir, safe_name)
                
                if not os.path.exists(dest_path):
                    print(f"  Copying: {local_path} -> {dest_path}")
                    shutil.copy2(local_path, dest_path)
                
                # Update HTML content
                # the new path should be relative to the html file
                new_url = f"assets/site_images/{urllib.parse.quote(safe_name)}"
                new_content = new_content.replace(match, new_url)
            else:
                print(f"  WARNING: File not found locally: {local_path}")
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == "__main__":
    copy_and_update_assets()
