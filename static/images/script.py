import os

# Configuration: Path to your templates folder
# Since this script is in v2/static/images, we go up two levels (../../) to get to v2/templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'templates'))

# Mapping of Old Filenames -> New Filenames
IMAGE_REPLACEMENTS = {
    'contact.jpg': 'contact.webp',
    'ems_emros.png': 'ems_emros.webp',
    'energy.png': 'energy.webp',
    'energy_emros.png': 'energy_emros.webp',
    'grms.png': 'grms.webp',
    'grm_emros.png': 'grm_emros.webp',
    'guest-presence.png': 'guest-presence.webp',
    'home-2.png': 'home-2.webp',
    'home-3.png': 'home-3.webp',
    'home-4.png': 'home-4.webp',
    'home-5.png': 'home-5.webp',
    'home-6.png': 'home-6.webp',
    'privacy_emros.png': 'privacy_emros.webp',
    'sensor_emros.png': 'sensor_emros.webp',
    'sol-privacy-service-1.png': 'sol-privacy-service-1.webp',
    'sol-privacy-service-2.png': 'sol-privacy-service-2.webp'
}

def update_templates():
    if not os.path.exists(TEMPLATES_DIR):
        print(f"Error: Directory '{TEMPLATES_DIR}' not found.")
        print(f"Current script location: {BASE_DIR}")
        return

    print(f"Scanning directory: {TEMPLATES_DIR}...")
    
    count = 0
    # Walk through the directory to find HTML files
    for root, _, files in os.walk(TEMPLATES_DIR):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    changes_in_file = 0
                    
                    # Perform replacements
                    for old_img, new_img in IMAGE_REPLACEMENTS.items():
                        if old_img in new_content:
                            new_content = new_content.replace(old_img, new_img)
                            changes_in_file += 1
                            print(f"  [+] Replaced '{old_img}' -> '{new_img}' in {filename}")

                    # Write back only if changes were made
                    if changes_in_file > 0:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"✓ Updated {filename} ({changes_in_file} changes)")
                        count += 1
                    else:
                        print(f"- No changes needed in {filename}")
                        
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    print(f"\nDone! Updated {count} files.")

if __name__ == "__main__":
    update_templates()